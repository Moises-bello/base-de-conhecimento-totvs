---
article_id: 35710630949271
category: Financeiro - Contas a Pagar
content_hash: 8763a6b62aba637418eb5af08069b9e4ef4426c86b97d7106398f0b8e97a4d1c
fetched_at: '2026-06-28T22:38:07.065948+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como realizar importação
  de titulo PA via MILE
type: support-article
updated_at: '2025-10-20T09:58:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35710630949271-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-realizar-importa%C3%A7%C3%A3o-de-titulo-PA-via-MILE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35710630908951) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como realizar importação de titulo PA via MILE?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
1- Acessar o módulo Configurador **(SIGACFG)** - Acessar o caminho **Ambiente >> Aceleradores >> Mile >> Layouts;**

2- Clicar em Incluir **"Importação"**.

Realizar o preenchimento dos dados de acordo conforme exemplo do print a seguir.

**Geral:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35710630910999)

**Formação do Arquivo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35710617554327)

**Dados do Canal:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35710617555223)

**Campos:** Preencher os campos obrigatórios do cadastro de um titulo PA, exemplo:

**OBS: Os campos AUTBANCO, AUTAGENCIA e AUTCONTA são os campos que receberam o código do banco, agencia e conta da movimentação do PA.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35710617559447)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35710630917911)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35710630922391)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35710617565591)

3- Abrir um Bloco de Notas e realizar a composição dos dados que cada campo irá receber, definidos na Aba campos de acordo com a sequencia e o separador seja por **"Ponto e Virgula ou PIPE".**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35710617570199)

4- Acessar a rotina de **FINA050 (Contas a pagar)**, ir em **Outras ações > Outros >> Importar**

Selecionar o arquivo **.TXT** gravado e realizar a Importação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35710617571095)

5- Tela de Processamento para informar se foi concluído com sucesso ou se apresentou algum incidente na importação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35710617571607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35710630928919)

**Saiba mais:**

[Framework - Linha Protheus - MILE: Model Integrator Layout Engine](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028814432-Framework-Linha-Protheus-MILE-Model-Integrator-Layout-Engine)

[Mile Importação e Exportação do Layout](https://tdn.totvs.com/pages/releaseview.action?pageId=423932458)
