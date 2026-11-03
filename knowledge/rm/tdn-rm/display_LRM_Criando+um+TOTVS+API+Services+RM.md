---
content_hash: 1b3bb248f82ff789bfbcfa805369a36111dce77009b101484e2372560d6483e1
fetched_at: '2026-06-29T00:11:13.429155+00:00'
page_id: '66126183'
product: rm
source: tdn-rm
title: Criando um TOTVS API Services RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Criando+um+TOTVS+API+Services+RM
version: 14
---

true

### Criando um TOTVS API Services versão 12.1.2306

Com a versão 12.1.2306, não será mais necessário informar manualmente o nome de usuário e senha, pois o RM enviará automaticamente essas informações para o TOTVS API Services.

Conforme na outras versões abaixo o processo é o mesmo. No exemplo abaixo iremos Selecionar o Correios - Pesquisa de CEP.

"No exemplo dos Correios, o parâmetro de entrada será o CEP. Se estivéssemos lidando com um serviço da Receita Federal, o parâmetro seria o CNPJ ou CPF, dependendo da situação."

"Para buscar um endereço, arraste o parâmetro CEP para o campo CEP da visão ou selecione a opção 'Informado pelo usuário'.

Em seguida, todos os campos relacionados ao endereço serão exibidos com uma seta indicando os resultados.

Para selecionar o endereço correto, clique na seta para abrir a janela de itens, onde você poderá escolher o endereço, bairro e outras informações relevantes. Certifique-se de selecionar as opções corretas para cada campo."

Após as configurações acima, a janela do TOTVS API Services para a opção de Resultado (saída) ficará com os itens selecionados.

Após clicar no ícone de Salvar, o TOTVS API Services já poderá ser utilizado.

Iremos agora usar a funcionalidade de Correios para obter as informações mapeadas.

Informe o Cep e clique em Avançar.

Clique em Ok para as informações do CEP vincular ao mapeamento feito.

Ao retornar o RM é preenchido corretamente, conforme o mapeamento feito.

Atenção

Na versão 12.1.2306, houve uma mudança nos nomes dos menus que antes eram referentes ao Mashup. Agora, esses menus foram renomeados para TOTVS API Services. Caso tenha alguma dúvida ou precise de ajuda para encontrar os menus que procura, nossa equipe de suporte estará pronta para ajudá-lo.

### Criando um Mashup Versões 12.1.2302, 12.1.2209, 12.1.2205 até 12.1.31

IMPORTANTE

A partir das versões informadas abaixo, para utilização dos serviços pagos do Mashup é preciso informar a API-KEY (Chave de autenticação - Token) disponibilizada no painel do cliente na Totvs Store. A utilização dos demais serviços é independente do token.

Mais informações sobre os serviços pagos acesse: <https://www.totvs.com/totvs-api-mashup/>

**Alteração disponível nas seguintes versões e patches:**

12.1.31, a partir do Patch 294

12.1.32, a partir do Patch 241

12.1.33, a partir do Patch 177

12.1.34, a partir do Patch 100 e versões mais atuais

Para estas versões veja a documentação, 

   
**Desenvolvimento/Procedimento**  
   
Para configurar o Mashup, abra qualquer janela que possui a função **Processos** **-> Mashups**   
Ex: Cadastro de Cliente/Fornecedor.   
   
Na tela que se segue criem uma nova conta no TOTVS Mashups e informe os dados necessários.   
   
  
Caso já tenha uma conta criada, somente fazer o login no servidor: mashups.totvs.com.br. Para criar uma nova conta, preencher os campos abaixo:   
  
  
   
   
Após criar a conta, será enviado um email de confirmação do cadastro.  
Após a ativação do usuário cadastrado, deve-se efetuar o Login.   
   
  
  
  
  
   
  
  
Clique em "Fazer integração dessa Tela com um novo Mashup" e na tela que segue procurem pelo serviço desejado.  
No nosso exemplo, solicitamos o serviço dos Correios.   
   
  
  
A parametrização é feita em duas etapas, Parâmetros (entrada) e Resultado (saída)   
   
No nosso exemplo dos Correios, o Parâmetro (entrada) será CEP. Se o serviço fosse da Receita Federal, por exemplo, seria CNPJ ou CPF.  
   
  
  
  
Arraste o parâmetro CEP para o campo CEP da visão ou selecione a opção "Informado pelo usuário"   
Após arrastar o Parâmetro (entrada), para o campo CEP, todos os demais campos relacionado com endereço, irá aparecer uma "seta" (print abaixo) que será os Resultados (saída). Clique na seta para abrir a janela de itens (endereço, bairro e etc.) e selecione a opção correta para o campo.   
  
  
   
  
  
  
  
Após as configurações acima, a janela do Mashup para a opção de Resultado (saída) ficará com os itens selecionados.   
   
  
  
Após clicar no ícone de Salvar, o Mashup já poderá ser utilizado.   
Preencha o CEP do endereço na janela de Cadastro. Após o preenchimento salve a alteração.   
  
  
   
Após salvar a alteração, execute o Mashup: Processo > Mashup > Correios.  
Será iniciada a busca no servidor.  
   
   
Após clicar no botão Finalizar, os dados da visão serão atualizador com os dados do Resultado.   
Caso a opção marcada na configuração do Mashup para a entrada de parâmetro foi "Informado pelo usuário", O CEP deverá ser preenchido manualmente:  
   
O mesmo resultado será retornado.

|  |  |
| --- | --- |
|  | **Para maiores informações:** Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
