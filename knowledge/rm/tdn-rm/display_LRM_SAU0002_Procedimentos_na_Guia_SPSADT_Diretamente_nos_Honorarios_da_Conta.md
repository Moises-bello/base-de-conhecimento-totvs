---
content_hash: d6181adc7129f49163c2a654352627d32b6563a191cf76791707ea0337fd30df
fetched_at: '2026-06-29T00:05:59.742646+00:00'
page_id: '192086910'
product: rm
source: tdn-rm
title: SAU0002_Procedimentos_na_Guia_SPSADT_Diretamente_nos_Honorarios_da_Conta
type: documentation
url: https://tdn.totvs.com/display/LRM/SAU0002_Procedimentos_na_Guia_SPSADT_Diretamente_nos_Honorarios_da_Conta
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO HOSPITALAR |
| **Versões:** | 11.8x e 12.1.x |
| **Ocorrência:** | Como fazer com que os procedimentos lançados na guia SP/SADT caiam direto na conta do paciente, na aba "Honorários"? |
| **Passo a passo:** | 1° Passo - Parametrizar.  Acesse o Menu Opções / Parâmetros / Parâmetros Gerais  Na aba "Registro e Controle 2", marque os checkbox e defina o centro de custo Default para o lançamento.    2°Passo - Configurar as condições Contratuais com o convênio específico.  Acesse o menu Cadastros / Faturamento / Condições Contratuais com Convênios  Escolha o convênio desejado  Na aba "Parâmetros 1", marque o checkbox:    3° Passo - Definir a faixa de codificação  Acesse o Menu Cadastros / Faturamento / Padrões de Faturamento e Codificação  Escolha o padrão de codificação usado para o convênio com o qual gostaria que ocorresse o lançamento automático  Na aba "Códigos 1"  Supondo que o procedimento desejado seja o procedimento: 10.10.1039  Ele deve estar inserido em alguma das seguintes faixas:    4° Passo - Realize os testes.  No registro de atendimento, na aba "Guia/Autorização", lance uma guia de SP/SADT com o procedimento 10.10.1039.  Em seguida, verifique se o lançamento foi incluso na conta do paciente, na aba Honorários |

divs
