---
article_id: 360034847234
category: RH - Provisão
content_hash: 795e373340c918d720cf1ca429a235f8e0a613545ebf8f6af76596ff86e4c4e0
fetched_at: '2026-06-28T22:43:55.800295+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Devem ser Preenchidos os Campos %Prov.13º,
  %Prov.Férias e %Prov.Resc. na tabela S037
type: support-article
updated_at: '2025-06-17T20:32:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034847234-RH-Linha-Protheus-GPE-Como-Devem-ser-Preenchidos-os-Campos-Prov-13%C2%BA-Prov-F%C3%A9rias-e-Prov-Resc-na-tabela-S037
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17492943366167)**Tempo aproximado para leitura:**00:02:00 min**

**Dúvida**Como Devem ser Preenchidos os Campos %Prov.13º, %Prov.Férias e %Prov.Resc. na tabela S037?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir do Release 12.  
  
**Solução**Estes campos são utilizados para um cálculo de "Provisão Sintética" na Folha de Pagamento, para os usuários que não realizam o Cálculo das Provisões de Férias e 13º salário pela rotina GPEA070.  
Quando os campos forem preenchidos, no cálculo da folha de pagamento será apresentada as verbas com identificadores de cálculo:  
  
0194 - Prov. Férias p/ Custo .   
0195 - Prov. 13º Sal. p/ Custo.   
0196 - Prov. Rescis. p/ Custo .   
  
**Importante**: Estas verbas devem ser incluídas como Base - Provento, e sem nenhuma incidência.

1. Acesse: Atualização / Definição de Cálculo / Manutenção de Tabelas (GPEA320) / Selecione a Tabela S037 e clique em Alterar;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17492759691671)  
  
2. No Campo **%Prov.13º,** informe o percentual a ser aplicado sobre as verbas mensais da folha de pagamento para cálculo dos valores de provisão 13º salário;  
  
3. No Campo **%Prov.Férias,** informe o percentual a ser aplicado sobre as verbas mensais da folha de pagamento para cálculo dos valores de provisão férias;  
  
4. No Campo **%Prov.Resc**, informe o percentual a ser aplicado sobre as verbas mensais da folha de pagamento para cálculo dos valores de provisão rescisão.  
  
**Importante***:*- Estes campos não determinam o Percentual de INSS da Provisão, e sim o percentual à ser aplicado sobre as verbas da Folha de Pagamento, para cálculo da provisão.  
- Não há obrigatoriedade no preenchimento destes campos, caso a provisão deva ser calculada com base no Salário, Adicionais e Médias do funcionário, estes campos devem estar zerados e as provisões devem ser processadas pela rotina GPEA070.

**Saiba Mais:**

[Funcionalidade do Campo RV\_CUSTO no Cadastro das Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6503898874007-RH-Linha-Protheus-GPE-Funcionalidade-do-campo-RV-CUSTO-no-cadastro-de-verbas?source=search)   
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
