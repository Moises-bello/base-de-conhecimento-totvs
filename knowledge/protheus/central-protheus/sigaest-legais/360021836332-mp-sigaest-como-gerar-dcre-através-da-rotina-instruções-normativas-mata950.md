---
article_id: 360021836332
category: SIGAEST - LEGAIS
content_hash: 222d7ed820f514bf0994e2e955776e6b7b035ad2a27890c4b3f44c1da8b2c061
fetched_at: '2026-06-28T22:38:51.928663+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: MP - SIGAEST - Como gerar DCRE através da rotina Instruções Normativas (MATA950)?
type: support-article
updated_at: '2021-04-28T15:12:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021836332-MP-SIGAEST-Como-gerar-DCRE-atrav%C3%A9s-da-rotina-Instru%C3%A7%C3%B5es-Normativas-MATA950
---

**Dúvida**

Como gerar DCRE através da rotina Instruções Normativas (MATA950)?  
  
**Ambiente**

Microsiga Protheus – Estoque/Custos – A partir da versão 11.80  
  
**Solução**

Para solucionar essa dúvida, realize os seguintes passos:

Acesse o módulo **Livros Fiscais (SIGAFIS)**, opção **Miscelânea/Arq. Magnéticos/Instr. Normativas (MATA950)** e configure os parâmetros da rotina, conforme indicado a seguir:

* **Data Inicial**

Informe a data inicial para processamento da Instrução Normativa.

* **Data Final**

Informe a data final para processamento da Instrução Normativa.

* **Instr. Normativa?**

Informe o nome do arquivo de configuração, sem a extensão .INI. Exemplo: **SIMPLESN .**

* **Arq. Destino?**

Informe o nome do arquivo de destino. Exemplo: **SIMPLESN.TXT**.

* **Diretório Destino?**

Informe o nome do diretório em que será gravado o arquivo texto gerado a partir da apuração. Exemplo: **C:\TXT\**.

* **Seleciona Filiais?**

Informe se deseja selecionar as filias que serão processadas. Ao informar **Não**, apenas a filial corrente será considerada; ao informar **Sim**, o sistema apresenta uma tela para seleção das filiais a serem consideradas.

* **Aglutina Obrigação?**

Informe se deseja algutinar a informação das filias que serão processadas, gerando um único arquivo. Ao informar **Não**, a informação das filiais continuará sendo gerada como anteriormente; ao informar **Sim**, o sistema aglutinará a informação das filiais selecionadas em um arquivo único.

Confira os dados e finalize.

Importante: Quando a pergunta "Aglutina Obrigação" está com conteúdo igual a sim, as filiais serão exibidas conforme ordem do CNPJ, e não conforme ordem do código da filial.

**Saiba Mais**

*[Instruções Normativas – Geração de Arquivos Magnéticos](https://tdn.totvs.com/pages/viewpage.action?pageId=185753759)*

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
