
<body>
<header align="center">
<nav align="center">
<span align="center" text-align="center">
<img src="https://github.com/bryanqf/badges/blob/main/Bs4.svg" alt="Bs4" style="display: inline-block; margin-right: 5px;">
<img src="https://github.com/bryanqf/badges/blob/main/Pandas.svg" alt="Pandas" style="display: inline-block; margin-right: 5px;">
<img src="https://github.com/bryanqf/badges/blob/main/Selenium.svg" alt="Selenium" style="display: inline-block; margin-right: 5px;">
<img src="https://github.com/bryanqf/badges/blob/main/Pyodbc.svg" alt="Pyodbc" style="display: inline-block;">
</span>
</nav> 
<h1 align="center"> Scrapping de todas as Vagas disponíveis no Site hipsterJobs</h1>
</header>
<p text-align="center">A proposta desse projeto é realizar um WebScrapping completo de todas as vagas disponíveis no site HipsterJobs. Utilizando a biblioteca Selenium e BS4</p><br>    
<p text-align="center">No inicio eu queria apenas testar algumas funcionalidades da biblioteca BeautyfulSoap, mas após me fascinar um pouco sobre possibilidade de encher um banco de dados usando o ORM SQLalchemy, 
      acabei mudando a proposta do projeto.
</p><br>
  
<h2>Como funciona o projeto:</h2>
<h3> Banco de dados</h3>
<p>° Primeiro é feito uma conexão com o meu banco de dados SQL Server que a principio está sem nenhuma tabela.</p>
<p>° Depois crio um modelo para explicitar cada tabela que será usada no banco.<br> Obs: Nesse modelo eu especifico as tabelas que serão usadas, os tipos de dados e as relações entre elas. 
Caso a tabela não exista uma função irá checar e criar.
<br>1: Nesse caso por se tratar de um projeto relativo a vagas de emprego, criei uma tabela chamada local, com id auto incrementado, e o local.
<br>2: Também a tabela empresa, que tem o id auto incrementado, o nome da empresa, e recebe o valor de id do local da tabela local.
<br>3: E por ultimo irá criar a tabela Vagas que tem també o id auto incrementado, a vaga, o tipo de relação de trabalho, o link do site, e o id da empresa que virá da tabela empresa.
</p>
<h3>Scrapping</h3>
<p>° Essa parte Utiliza basicamente a lib Selenium</p>
<p>1: Abre o navegador com a função abre_navegador()
<br>2: Confere quantas vagas existem no site, e cria um laço de repetição até que a quantidade de vagas seja >= as que foram entradas, ou não ache mais o botão de carregar mais.
<br>3: Após encontrados todas as vagas da pagina, Dispara a função cria listas.<br>
3.1: Com todas as vagas disponíveis para o acesso, temos então a inspeção dos dados.
<br>3.2: Para cada vaga, são jogados os dados dentro da classe beautifulsoap e retonam a variavel soap
<br>3.3: Com o soap utilizo funções de busca pra encontrar cada dado necessário para preencher as tabelas anteriores o os coloco dentro de um dicionario e faço um append para a lista chamada vagas.
<br>3.4: Transformo essa lista em um dataframe pandas em seguida.
</p>
<h3>Instanciando todas as vagas como objetos para a tabela.</h3>
<p>
° Nessa parte eu importo os modelos criados das tabelas anteriomente. e crio algumas funções para instanciar as classes com os dados do Dataframe pandas.
<br>1:A função local recebe um set chamado set_local, que é usado para evitar que informações duplicadas. essa função recebe os dados do dataframe dentro de um set coloca no lugar indicado na tabela e adiciona a sessão SQLAlchemy usando o comando session.add.
<br> 1.1: Em seguida utiliza o session.flush() para gerar o ID do local e inserir em um dicionario como valor, e fecha a sessão com a função fecha_sessao().
<br> 2: As empresas também recebem um set_empresas, para evitar duplicadas, mas as empresas utiliza no lugar da string uma tupla, que também usa o local em que a empresa está localizada. 
<br>2.1: Então existem algumas empresas com o mesmo nome mas lugares diferentes. a empresa utiliza o ID que é provido no dicionário local, então utilizo o nome do local que está na tupla para conseguir o id do local que está salvo no dicionário.
<br>2.2: Em seguida instancio a empresa com o nome e o id que vem do dicionario de locais.
<br>2.3: e utilizo o session.flush() para pegar o id que foi gerado da empresa e salvar em outro dicionário
<br>3: E por ultimo instancio a vaga recebendo basicamente dos os valores em uma lista, e recebendo também o dicionário da empresa com o id.
<br>3.1: Nesse caso coloco os valores na tabela e coloco também o id da empresa para fazer a referencia faço o session.add e fecho a conexão com a função fecha_sessao()
</p>

    
    

</body>
