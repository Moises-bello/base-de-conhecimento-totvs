---
article_id: 360050216394
category: Gestão de Transportes (TMS)
content_hash: 70930bd65168c6cf0485903ef755709248c70de18c755981e619480815abb3f4
fetched_at: '2026-06-28T22:45:27.403401+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como calcular CTe com PIS e COFINS
type: support-article
updated_at: '2022-07-19T12:55:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050216394-Log%C3%ADstica-Linha-Protheus-TMS-Como-calcular-CTe-com-PIS-e-COFINS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Qual a parametrização necessária para emitir um **CTe** calculando o **PIS** e **COFINS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para que o cálculo de **PIS** e **COFINS**, seja realizado corretamente, é necessário que alguns cadastros tenham alguns campos destacados conforme apresentado a seguir:

1. **Produto de Calculo**. Acessar o menu **Atualizações/Cadastros/Produtos - MATA010.**Este produto é utilizado para a escrituração do documento que será emitido no **TMS**e é vinculado ao cadastro de configuração de documento localizado no menu **Atualizações/Documentos e Regras/Config. Documentos - TMSA150**.  
     
   Neste cadastro devem ser considerados os campos:  
   Aba **Impostos:  
   B1\_PIS - Retem PIS**= Sim;  
   **B1\_COFINS - Retem COF**= Sim;  
   **B1\_PCOFINS - Perc. COFINS**= Informar o percentual do **COFINS;**  
   **B1\_PPIS - Perc. PIS**= Informar o percentual do **COFINS.**
2. **Cliente.**Acessar o menu **Atualizações/Cadastros/Clientes - MATA030.**O Cliente devedor do frete deve ter estes campos definidos:  
   Aba **Fiscais:  
   A1\_RECCOFI - Rec. COFINS** = Sim;  
   **A1\_RECPIS - Rec. PIS** = Sim.
3. **TES.**Acessar o menu **Atualizações/Cadastros/Tipos de Entradas e Saídas - MATA080.**A **TES** deve ser vinculada no cadastro de Regra de Tributação localizado no menu **Atualizações/Documentos e Regras/Regras Tributação - TMSA410.**Para que a **TES** realize os cálculos do **PIS** e **COFINS** é necessário destacar os campos abaixo:  
   Aba **Impostos:  
   F4\_PISCOF - PIS/COFINS** = Ambos;  
   **F4\_AGRPIS - Agr. PIS** = Selecionar conforme necessidade;  
   **F4\_AGRCOF - Agr. COFINS** = Selecionar conforme necessidade.

**Glossário****COFINS** - Contribuição para Financiamento da Seguridade Social  
**CTe** - Conhecimento de Transporte Eletrônico **PIS** - Programas de Integração Social e de Formação do Patrimônio do Servidor Público**TES** - Tipos de Entrada e Saída  
**TMS** - Gestão de Transporte
