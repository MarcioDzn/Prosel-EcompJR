<div align="center">

# Prosel-EcompJR

</div>

<A name= "Intr"></A>

# Introdução

<div align="justify">
A Ecomp Jr, empresa júnior de Engenharia de Computação da UEFS, identificou uma necessidade urgente de aprimorar a gestão de tarefas entre seus membros e administradores. O sistema atual, baseado em processos manuais, gera dificuldades de organização e acompanhamento, impactando diretamente na eficiência das atividades. Assim, este projeto tem como objetivo desenvolver uma aplicação de lista de tarefas (to-do list) que proporcione uma solução prática e intuitiva. Utilizando React.js para o front-end, FastAPI para o back-end e SQLite como banco de dados, a aplicação permitirá o gerenciamento de tarefas pelos usuários e o controle de usuários por administradores. Com isso, a Ecomp Jr espera otimizar seus processos internos, facilitando o acompanhamento e a execução das atividades diárias.
</div>

# Sumário
- <A href = "#Intr">Introdução</A><br>
- <A href = "#Exec">Como Executar</A><br>
- <A href = "#Prot">Prototipação</A><br>
- <A href = "#Front">Front-End</A><br>
- <A href = "#Back">Back-End</A><br>
- <A href = "#Inte">Integração</A><br>
- <A href = "#Conc">Conclusão</A><br>

<A name="Exec"></A>
# Como Executar

## Etapas:

### 1. Configuração do Ambiente:
   
  - Para utilizar essa aplicação, é essencial que o ambiente esteja devidamente configurado. Primeiramente, é necessário ter a linguagem Python instalada no sistema, pois a partir dela será possível realizar a instalação do FastAPI, juntamente com ferramentas como Poetry e Pyenv, utilizando o comando pip install. Além disso, é fundamental dispor de um ambiente de desenvolvimento integrado (IDE), que facilitará a execução dos comandos e o gerenciamento da aplicação de maneira eficiente. Outro ponto a ser observado é a instalação do Node.js, indispensável para criar e rodar o front-end em React. Com essas dependências devidamente configuradas, o desenvolvimento e a execução da aplicação ocorrerão de forma fluida e organizada.
     
### 2. Obtenção do Código Fonte:

   - **Clonagem do Repositório:** Você pode utilizar o seguinte comando no terminal para adquirir a aplicação:                                          

           git clone https://github.com/MarcioDzn/Prosel-EcompJR.git.
     
   - **Download do Código Fonte:** Caso não tenha o Git na máquina, você pode fazer o download desse repositório manualmente. Vá até o canto superior, selecione "Code" e depois "Download ZIP", e então extraia o arquivo ZIP na sua máquina.

### 3. Configuração da Aplicação:

 # Back-End:
   Primeiramente, para conseguirmos executar a API, devemos executar esses passos respectivamante:

   1.     cd todo_list
   2.     poetry install
   3.     poetry shell
   4.     alembic upgrade head
   
   `Observação:` Para que essa etapa ocorra normalmente é necessário que você esteja com o projeto aberto na pasta principal.

 # Front-End:

 > :construction: Em construção :construction:

### 4. Execução da Aplicação:

 # Back-End:
   Após ter realizado adequadamente a configuração da aplicação, podemos iniciar a API através do comando:  
 
       fastapi dev todo_list/app.py
   Pronto, agora você poderá fazer testes com a API clicando em Ctrl e na rota API docs conforme está ilustrado na Figura 1.

   <div align="center">
   
   ![Figura 1](imagens/backend/fastapi.png)
   <br/> <em>Figura 1. Imagem API em execução.</em> <br/>
   
   </div>
   
# Front-End:

  > :construction: Em construção :construction:

<A name="Prot"></A>
# Prototipação

...

<div align="center">
   
   ![Figura 8](Imagens/menucliente.png)
   <br/> <em>Figura 2. .</em> <br/>
   
   </div>

  <div align="center">
   
   ![Figura 9](Imagens/opcao2cliente.png)
   <br/> <em>Figura 3. .</em> <br/>
   
   </div>

   <div align="center">
   
   ![Figura 10](Imagens/opcao5cliente1.png)
   <br/> <em>Figura 4. .</em> <br/>
   
   </div>

   <div align="center">
   
   ![Figura 11](Imagens/opcao1cliente.png)
   <br/> <em>Figura 5. .</em> <br/>
   
   </div>

   <div align="center">
   
   ![Figura 12](Imagens/opcao5cliente.png)
   <br/> <em>Figura 6. .</em> <br/>
   
   </div>

   <div align="center">
   
   ![Figura 13](Imagens/opcao4cliente.png)
   <br/> <em>Figura 7. .</em> <br/>
   
   </div>

   <div align="center">
   
   ![Figura 14](Imagens/opcao3cliente.png)
   <br/> <em>Figura 8. .</em> <br/>
   
   </div>

   <div align="center">
   
   ![Figura 15](Imagens/opcao5cliente2.png)
   <br/> <em>Figura 9. .</em> <br/>
   
   </div>

<A name="Front"></A>
# Front-End

> :construction: Em construção :construction:

<A name= "Back"></A>
# Back-End

...

<A name= "Inte"></A>
# Integração

> :construction: Em construção :construction:
 
<A name="Conc"></A>
# Conclusão

<div align="justify">
O desenvolvimento desta aplicação de lista de tarefas para o processo seletivo da EcompJr, representou uma oportunidade de profundo aprendizado técnico e colaborativo para todos os coloradores do projeto. A experiência também proporcionou um mergulho no desenvolvimento fullstack, envolvendo React.js para o Front-End, FastAPI para o Back-End e SQLite para o Banco de Dados, além de aprimorar habilidades de trabalho em equipe e organização de projetos. Além disso, ao longo do processo, o entendimento sobre a importância da segurança de dados, da prototipação e do uso de boas práticas no código ficou mais claro, demonstrando como essas etapas impactam diretamente na qualidade final do produto. 
</div> 
