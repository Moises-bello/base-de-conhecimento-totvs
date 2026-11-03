---
article_id: 360018682472
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: e876f0b023244a12a715785263d1da6aa5868ea009a3e1d449292d0bdeb4f5a2
fetched_at: '2026-06-28T22:45:20.905661+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial -  Painel eSocial - Erro de schema "No
  matching global declaration avaivable for the validation root
type: support-article
updated_at: '2026-06-26T12:08:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018682472-RH-Linha-Protheus-TAF-eSocial-Painel-eSocial-Erro-de-schema-No-matching-global-declaration-avaivable-for-the-validation-root
---

**Dúvida**  
Ao tentar transmitir os eventos do eSocial, é apresentado erro de SCHEMA:

*Erro de schema "No matching global declaration avaivable for the validation root.*

Exemplo de erro que pode ocorrer para os clientes que estão alterando de **leiaute eSocial:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19296567685399)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - e-Social - Painel Esocial do Futuro - Todas as versões

**Causa**  
Se o cliente estiver com o erro de Schema apresentado acima, independente do leiaute, solução abaixo será a mesma:

**Solução**

Para solucionar essa ocorrência, será necessário alterar o parâmetro **MV\_TAFVLES** para **S\_01\_03\_00** ou **S\_01\_02\_00** (conforme a atualização e necessidade do cliente) e estar com o TAF e TSS atualizados com os pacotes abaixo:

**1. Atualização, Expedição Contínua:**

Cliente no release 12.1.2210, 12.1.2310, 12.1.2410 e 12.1.2510, utilizem o link de atualização abaixo, caso não estejam atualizados:

[Automação Fiscal - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)

**Atenção:** Esta atualização possui dicionário de dados, é necessário rodar o UPDDISTR e UPDTAF.

**2. Atualizar TSS e Schemas:**

Se o ambiente não estiver atualizado, TSS e Schemas, utilize a documentação abaixo, que contém todos os links necessários:

[Automação Fiscal - ATUALIZAÇÃO - Links para atualizar o TSS - Transmissão de Documentos Eletrônicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7658806742679)

**5. Alterar o parâmetro MV\_TAFVLES no TAF:**

#### Link para orientação:

[Automação Fiscal - ATUALIZAÇÃO - Como atualizar a versão do layout no TAF E-social?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18585564590999)

**ATENÇÃO:** Para clientes que realizam a integração com o SIGAGPE, será necessário alterar também o parâmetro MV\_VLESOC.

**OBSERVAÇÃO:**

Se o registro (evento) no TAF, foi integrado em um leiaute diferente do configurado no parâmetro MV\_TAFVLES, será necessário excluir o evento no TAF e integrar o registro novamente do ERP (GPE/RM/Datasul) para o TAF;
