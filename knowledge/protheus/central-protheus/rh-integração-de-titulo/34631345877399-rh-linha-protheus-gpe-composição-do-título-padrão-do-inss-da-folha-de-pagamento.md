---
article_id: 34631345877399
category: RH - Integração de Titulo
content_hash: 676a03fe5d29d769be265f5a0403738b305b5210a222e1ffb028e40f7ecc5485
fetched_at: '2026-06-28T22:43:37.159136+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Composição do Título Padrão do INSS da Folha de
  Pagamento
type: support-article
updated_at: '2025-09-02T20:52:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34631345877399-RH-Linha-Protheus-GPE-Composi%C3%A7%C3%A3o-do-T%C3%ADtulo-Padr%C3%A3o-do-INSS-da-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34631331276567) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Quais são as verbas que compõem o Título Padrão de INSS de Folha de Pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**  
Utilizando a opção padrão de Título de INSS - Folha de Pagamento, o Protheus gera os valores de Resumo da Folha (tabela SRZ) a partir das tabelas de Movimento do Período (SRC) / Histórico de Movimentos (SRD), efetuando processamento por Tipo de Contrato, e carrega os dados das tabelas S037 (Encargos da Empresa), S038 (Outras Entidades) e verbas em S035 (Complemento GPS) para gerar o título à partir das verbas abaixo:

    0148 INSS Empresa  
    0149 Percentual de Terceiros  
    0150 Percentual Acidente Trabalho (exceto para produtor rural - Código de pagamento GPS 2607):  
    0064 INSS     
    0065 INSS Férias  
    0070 INSS 13º Salário  
    0351 Valor do INSS Pessoa Física  
    0354 Valor do INSS Pessoa Jurídica   
    deduzindo o Id 1412 Devolução INSS (Ferias com aliquota superior)

Para produtor rural, caso informadas na S035 as verbas de ID:  
    0315 Valor Produtor Rural PF  
    0316 Valor Produtor Rural PJ  
    e o percentual de encargo de SENAR (S038)

As deduções são compostas pelos proventos e descontos com Deducao da Guia de INSS=S (RV\_DEDINSS), além dos avos dos Ids abaixo conforme os parâmetros MV\_LIMDMAT e MV\_SALMGRP:  
    0040 Auxílio Maternidade   
    0407 Pagamento de Médias Auxílio Maternidade  
    1338 ATS Maternidade       
    1339 Insalubridade Maternidade  
    1340 Periculosidade Maternidade  
    1341 Adic. Cargo Confiança Maternidade  
    1342 Adic. Transferencia Maternidade

Para demissões no período, busca a verba de Id 0670-Deducao Salario Maternidade de 13o salario na GPS,  
e caso não encontre, calcula dedução de salário maternidade buscando nos valores da folha do período (SRC) os IDs:  
    0114 13º Indenizado na Rescisão  
    0115 13º Aviso prévio indenizado   
    0251 Média 13º Salário na Rescisão  
    0253 Media 13º sobre Aviso Indenizado na Rescisão

**Saiba Mais:**  
[Composição dos Títulos Padrões](https://tdn.totvs.com/pages/releaseview.action?pageId=976128352)   
[RH - Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
