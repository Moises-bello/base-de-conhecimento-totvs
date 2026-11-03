---
article_id: 360035825093
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 414ec6d64dcb271f6775615cdaebe7577fb372fae11d488d1b03cea05ac70915
fetched_at: '2026-06-28T22:37:21.467061+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como carregar um rateio
  contábil pré-configurado (Rateio Externo) em uma Medição ?
type: support-article
updated_at: '2022-05-19T21:08:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035825093-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-carregar-um-rateio-cont%C3%A1bil-pr%C3%A9-configurado-Rateio-Externo-em-uma-Medi%C3%A7%C3%A3o
---

**Dúvida**Como carregar um rateio contábil pré-configurado (Rateio Externo) em uma Medição ?

**Ambiente**Protheus – Gestão de Contratos – A partir da versão 12.1.17  
  
**Solução**É possível, no momento da medição do contrato, carregar rateios contábeis pré-cadastrados.

Para isso é necessário, primeiramente, cadastrar um rateio contábil na rotina "Atualizações->Rateios->Rateios Externos" (CTBA120) no Módulo Contabilidade Gerencial.

Exemplo de Cadastro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046862913/mceclip0.png)

Com o Rateio Externo cadastrado, na rotina Nova Medição (CNTA121), incluir uma medição para um contrato:

- Selecionar o Contrato;

- Selecionar a Planilha;

- Inserir a quantidade a ser medida:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046863353/mceclip4.png)

Verificar a aba "Rateio Contábil", e utilizar a opção "Outras Ações -> Rateio Pré-Configurado"

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046863193/mceclip1.png)

Selecionar o rateio pré cadastrado na janela que é aberta e confirmar:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046863253/mceclip3.png)

Verificar o carregamento automático que é realizado na aba "Rateio Contábil" conforme o rateio pré-configurado, já inserindo os valores na coluna "Vlr Moeda 1", rateando o Valor da Medição conforme os percentuais do Rateio Externo Pré-Configurado também carregados:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046863453/mceclip6.png)

Após isso, caso não for inserir mais nenhuma informação, a medição já pode ser confirmada.

Abaixo artigo relacionado à configuração de Rateios:

[MP - SIGACTB - IMPORTAÇÃO DE RATEIO EXTERNO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014885892-MP-SIGACTB-IMPORTA%C3%87%C3%83O-DE-RATEIO-EXTERNO-?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
