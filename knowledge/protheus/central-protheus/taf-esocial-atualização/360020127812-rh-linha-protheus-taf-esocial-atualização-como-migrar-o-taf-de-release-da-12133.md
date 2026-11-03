---
article_id: 360020127812
category: TAF - eSocial - Atualização
content_hash: b4dd454d677da0f545b6b743b56da7278d10ab9ccc2e4b441217c848762d3383
fetched_at: '2026-06-28T22:45:13.302287+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial  - ATUALIZAÇÃO - Como migrar o TAF de release
  da 12.1.33 para a release 12.1.2310 utilizando o atualizador? (SEGREGADO)
type: support-article
updated_at: '2026-06-25T12:25:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020127812-RH-Linha-Protheus-TAF-eSocial-ATUALIZA%C3%87%C3%83O-Como-migrar-o-TAF-de-release-da-12-1-33-para-a-release-12-1-2310-utilizando-o-atualizador-SEGREGADO
---

**Dúvida**

Como atualizar o TAF Segregado via executável?

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Atualização - À partir da versão 12.1.33

**ATENÇÃO!**

**O atualizador irá efetuar a virada automática para o release 12.1.2310, é obrigatória a utilização do [TOTVS License Server 3.2.0](https://tdn.totvs.com/display/framework/TOTVS%2BLicense%2BServer%2BVirtual).**

**À partir da release 12.1.33 o TAF passará a consumir licenças conforme material abaixo:  
<https://tdn.totvs.com/display/public/TAF/10+-+Licenciamento>**

**Antes de atualizar o seu ambiente, verifique atentamente os pontos abaixo:**

**Este atualizador, não efetua a atualização dos últimos pacotes, esta funcionalidade só servirá para efetuar migração de release para a release 12.1.2310.**

**Para que o TAF fique atualizado com as últimas atualizações, deverá seguir o material no fim deste artigo.**

* **Quais clientes podem utilizar o atualizador?**

+ O atualizador foi desenvolvido para clientes que utilizam o TAF como solução **"SEGREGADA"**, caso utilize algum módulo **Protheus** além do TAF, **O ATUALIZADOR NÃO DEVE SER UTILIZADO;**

* **IMPORTANTE:**
  + **DEIXE O ANTIVÍRUS DESABILITADO DURANTE A ATUALIZAÇÃO DO TAF;**
  + **Deixe somente o DBAccess ativo para realizar a atualização do sistema;**
    - **Obs.: Nos serviços do windows, o DBAcess deve estar com o tipo de inicialização automática e na Aba Recuperação, deixar todos os parâmetros com o valor "Não executar nenhuma Ação":  
      ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071263714)**

* **Sistema operacional:**

+ O **atualizador/instalador** foi projetado para rodar apenas em ambiente **Windows 64 bits**;
+ A arquitetura windows 32 bits foi descontinuado para novas atualizações;

* **Banco de dados:**

+ **SQL Server:**

- Verifique se o mesmo encontra com os parâmetros conforme documentação abaixo:

  [TAF - CONFIGURAÇÃO - Criando conexões via ODBC em 64 bits (Obrigatório)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034281974)

+ **Oracle:**

- Importante ressaltar que o ORACLE CLIENT deve ser com a arquitetura 64 bits;
- Como Configurar o Oracle para o TAF:
  * [MP - FRAME - Configurar Fonte de Dados (OCI) (Windows)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016077371-MP-FRAME-Configurar-Fonte-de-Dados-OCI-Windows-)

* **DBAccess:**

+ Se precisar converter o TAF DBAccess de 32 bits para 64 bits, veja a documentação abaixo:

  [TAF - DBACCESS - Alterar serviço TAF\_DBAccess de 32bits para 64bits](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042045853)
+ Caso Tenha o DBAccess em 64 bits, realize a atualização do DBAccess somente:  
  [TAF - ATUALIZAÇÃO - Como atualizar o DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034522854)

* **Estrutura de pastas TAF (Protheus):**

+ A estrutura de pastas deverá conter os diretórios conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057527633)

+ Dentro da estrutura \bin, deverá conter a mesma estrutura conforme imagem abaixo**:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056653634)

* **Arquivo de Configuração TAF e TSS (appserver.ini):**

+ O nome do ambiente deverá ser **[TAF]** conforme imagem abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057527733)

+ Para o TSS deverá conter **[SPED]:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056653794)

* **Permissões de usuário:**

+ Para executar o Atualizador, deverá verificar se o usuário atual do servidor possui permissões de troca de arquivos durante a atualização do sistema:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057527793)

* **Arquivos de LOG's:**

+ Acesse a pasta **APPSERVER** e exclua todos os arquivos com as extensões **\*.TSK, \*.LOG e \*.OLD**;

* Renomeie as pastas CFGLOG e HHTRG. Exemplo: **\_\_HHTRG** e **\_\_CFGLOG**;:  
  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403017858583)

* **Backups:**

+ É altamente recomendável que seja feito **backup** **da pasta de instalação do TAF de forma manual,**e de preferência salvar em outro disco, *pendrives* ou nuvem, ou da forma como preferir **(Lembrando que o atualizador também realiza backup automático)**;
+ Faça o backup por completo do seu **Banco de Dados do TAF e TSS** antes de rodar o atualizador;

* **Atualização:**

  + Simulação - Rodar em modo simulação em busca do possíveis erros, caso tenha, o Atualizador efetuará o ***rollback*** e informará qual o erro, para que o mesmo seja corrigido manualmente.   
      
    **Obs.:** No final desta documentação tem uma lista dos possíveis erros e quais são suas soluções.
  + Produção - Caso tenha sucesso na execução em modo simulação, deverá ser executado em modo **"Produção"** ou seja, efetuando as devidas alterações no dicionário de dados.

* **[INTEGRAÇÃO RM/DATASUL X TAF]**

  Após a atualização do TAF para a release 12.1.27, no arquivo appserver.ini do TAF na pasta **app**, será obrigatório a inserção da seção *[LICENSECLIENT]* com o endereço e porta para seu *license client.*

  **Exemplo:**[LICENSECLIENT]  
  SERVER=seu-ip-do-license  
  PORT=sua-porta-do-license

**Solução**

**Passos para atualizar o TAF e o TSS:**

1 - Verifique se a conexão com o banco de dados do TAF e o TSS já estão rodando em 64 bits, conforme listamos acima;

2 - Clique no link abaixo para realizar o download do atualizador:

<https://suporte.totvs.com/portal/p/10098/download#detail/695527>

3 - Após realizar o Download do Portal do Cliente da última versão, executar o arquivo baixado com permissões de Administrador:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056653914)

4 - Selecione a opção "Atualizar produtos já instalados". Clique em **Próximo:**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057527913)

5 - A imagem abaixo exibe a interface questionando quais produtos o cliente utiliza.

**Obs.:** Repare que **NÃO** é apresentada a opção Protheus, pois clientes deste produto **NÃO DEVEM UTILIZAR** o atualizador.

Caso clientes da linha Protheus prossigam com a operação, será aplicada a atualização de toda a sua base de dados e não somente do TAF.

Clique em **Próximo:**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056653994)

6 - Confirme a janela apresentada:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056654034)

7 - Termo de Aceite (Alerta de Processo crítico). Clique em **Próximo:**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056654094)

8 - Termo de Aceite (Leitura de Documentação). Clique em **Próximo:**

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056654194)

9 - Termo de Aceite (Backup). Clique em **Próximo:**

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057528113)

10 - Abaixo estão listados todos os ambientes do TAF/TSS que possuem a estrutura correta conforme os **pontos importantes (que são listados os caminhos que possuem a estrutura padrão e os serviços ativos no windows)** para atualização. Selecione o ambiente desejado e Clique em **Próximo:**

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057528273)

11 - A interface abaixo, foi criada para que seja informado os **dados do usuário e senha de acesso ao sistema do TAF**, para isso clique em "**Parâmetros da Instalação**":

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056655414)![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057529573)

12 - **Atenção:**Caso o ambiente não possua a seção **HTTP** contendo no final do atributo **PATH** o conteúdo fixo **http-root**([+infos](https://tdn.totvs.com/x/-RSLHg)), então será aberta a seguinte interface:

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056655874)

**Detalhe:** Informe a Porta HTTP utilizada para abertura das interfaces do TAF do Futuro

**TAF do Futuro**

O **Projeto TAF do futuro** tem como objetivo evoluir o produto gerando visões gerenciais para entrega de suas obrigações acessórias com uma melhor experiência do usuário, iniciamos pelo eSocial e REINF mas iremos replicar todo esse novo modelo de usabilidade para todas as obrigações contempladas pelo produto. Estamos utilizando o PORTINARI para essa reformulação ( [Saiba mais sobre o Portinari](https://portinari.io/)), isso nos permite evoluir muito principalmente a questão de usabilidade.

Clique em **Próximo**

13 - Informe o usuário e senha do TAF com permissão de Administrador e Clique em **Próximo;**

14 - Confirme a tela de Backup:

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057529613)

15 - Neste momento o atualizador irá executar suas funções para o processo de atualização do TAF e o TSS:

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057529653)![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057529733)

16 - Pode-se acompanhar os detalhes da atualização, através do botão **..** (ao lado da barra de progresso)

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056656054)

17 - Tela gerada ao Fim da Atualização com Sucesso.

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056656094)

18 - Após a atualização/migração de release do TAF, deverá executar a atualização do TAF de acordo com o material abaixo:  
[Automação Fiscal - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)
