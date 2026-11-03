---
article_id: 16139280116887
category: Materiais - Compras (SIGACOM)
content_hash: 38c5bb1cd4200be49101cb34cde06c439596de4f82eb3a8fa3087bdf99ede82d
fetched_at: '2026-06-28T22:41:25.484576+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - Validação de Processos Importador
  XML x Transmite
type: support-article
updated_at: '2023-08-31T15:21:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16139280116887-Cross-Segmentos-Totvs-Backoffice-Protheus-Valida%C3%A7%C3%A3o-de-Processos-Importador-XML-x-Transmite
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16139255709463) Tempo aproximado para leitura: 00:02 **Dúvida**

Validação de Processos para o uso da Ferramenta de Integração entre Importador Xml x TOTVS Transmite

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12  
  
**Solução**

**Relação de problemas mais recorrentes encontrados**

**1)** Conferir no cadastro da empresa no Portal do Transmite se está igual ao cadastro de Empresa do Protheus (SYS\_COMPANY) inclusive o número de CNPJ **(inserir prints em caso de abertura de tikets)**

**(qualquer alteração realizada na filial do Protheus, deve ser realizada da mesma forma no transmite, e para que o sistema reconheça a modificação, a Wizard deverá ser reprocessada)**

**2)** Registrar o parâmetro MV\_XMLHIST = .T. e rodar a rotina COLAUTOREAD novamente para devida gravação na tabela DHZ do histórico de IDs importados e/ou com erros. Validar se as tabelas DHW, DHY e DHZ estão sendo devidamente preenchidas com os dados corretos, no processamento da integração.

**3)** Validar se as chaves preenchidas nos parâmetros MV\_*XMLCID e MV\_*XMLSCEC estão corretas, igual ao portal do transmite **(inserir prints em caso de abertura de tikets)**

**4)** Entrar na tabela CKOCOL e validar se o registro se encontra na tabela.

**4.1** Validar o campo CKO\_FLAG  (**conteúdo = 0** (não processado), **conteúdo = 1** (registro integrado), **conteúdo = 2** (registro com erro), **conteúdo = 3** (documento duplicado)), mais detalhes do status na documentação a seguir: [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - COLABORAÇÃO - Legenda dos campos: DS\_STATUS, CKO\_STATUS, DS\_TIPO E CKO\_FLAG – Central de Atendimento TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037713954-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-COLABORA%C3%87%C3%83O-Legenda-dos-campos-DS-STATUS-CKO-STATUS-DS-TIPO-E-CKO-FLAG)

Consulte também nossa documentação com os possíveis erros apresentados no campo CKO\_FLAG /botão reprocessar quando acessado via rotina: [Erros (Códigos)](https://tdn.totvs.com/pages/releaseview.action?pageId=485869227)

**4.2** Verificar o campo CKO\_ORIGEM se está com o conteúdo "TRANSMITE" pois dessa forma será identificado que foi retornado e feito a importação via integração TOTVS Transmite.

**CASO NÃO SOLUCIONE  segue todos os fatores essenciais para operacionalizar a funcionalidade**:

**A)** Validar todos os critérios indicados nas documentações: [SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML) | [Integração Protheus x TOTVS Transmite](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7557934491159) e no vídeo [Importador XML X Totvs Transmite](https://www.youtube.com/watch?v=tiTTVw8rESc)

**B)** Validar a implementação e configurações definidas no [WIZARD IX09](https://tdn.totvs.com/x/o7guHg)

**C)** Validar o comportamento no ambiente teste com o [pacote Acumulado do módulo Compras](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099), e demais artefatos, atualizados: [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/): [Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) ou [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/): [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947528) ou [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1031460) | Smartclient: [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) ou [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1031469) | [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/).

*(Obs: O pacote do TSS está contido no acumulado devido necessidade de atualização do fonte COLAUTOREAD. Importante lembrar que é necessário atualizar o RPO e depois rodar o dicionário para criar as tabelas)*

**ATENÇÃO : É necessário que valide todos os fatores junto ao time que realizou a implementação e homologação da funcionalidade em seu ambiente.**

**CASO A INCONSISTÊNCIA PERSISTA**

Após validar os passos acima, caso a inconsistência persista encaminhar as informações abaixo para o suporte;

**1)** Um vídeo do processo completo sendo realizado assim poderemos testar de acordo com as particularidades de seu ambiente **(lembre-se de validar previamente se o sistema se encontra com as customizações desabilitadas e devidamente e atualizado)**

**2)** O arquivo .csv contendo os dados dos fontes em uso (inspetor de objetos).

**3)** Um número de telefone para contato, caso houver necessidade de uma explicação para melhor entendimento.

**4)** Enviar prints das empresas que estão cadastradas no Protheus (SYS\_COMPANY) e as que constam no portal do TOTVS Transmite.

**5)**  Realizar um teste com os Jobs sendo processados via Menu, verificando se ocorre algum erro em tela:

- Parar os serviços do Schedule;  
- Executar as rotinas COLAUTOREAD e SCHEDCOMCOL manualmente no menu (executa-las nessa ordem) e verificar se os XMLs saem da pasta IN para a LIDOS.  
Para inserir rotinas no menu verifique documentação a seguir: [MP - SIGACOM - (Importador XML ou Totvs Colaboração) | Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule?source=search)

Desta forma conseguiremos isolar a inconsistência, sendo ela devido ao Schedule ou Cadastros.

**6)**  Pare o Serviço do Protheus (realizar o processo a seguir no ambiente do Schedule caso possua o serviço separado do Protheus)

- Habilite a tag FWTRACELOG=1 na linha do environment do appserver.ini

- Apague o console.log e .bak (caso necessitar realize um backup previamente)

- Inicie o serviço em modo exclusivo

- Simule a inconsistência novamente e envie o novo console.log gerado

**SAIBA MAIS EM :**

**[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

**[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)**
