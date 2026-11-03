---
article_id: 360058178774
category: RH - Benefícios
content_hash: 12f2efa8af2ac2222628555abb30066889f20d645affa80bf84cddd68a7ae036
fetched_at: '2026-06-28T22:44:03.468779+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Ao informar o Código do Plano de Saúde/Odontológico
  nos Planos ativos ocorre a mensagem Código do Plano não cadastrado
type: support-article
updated_at: '2025-09-26T12:51:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058178774-RH-Linha-Protheus-GPE-Ao-informar-o-C%C3%B3digo-do-Plano-de-Sa%C3%BAde-Odontol%C3%B3gico-nos-Planos-ativos-ocorre-a-mensagem-C%C3%B3digo-do-Plano-n%C3%A3o-cadastrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33043973752343) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Ao informar o código do plano de saúde/odontológico na rotina de Planos Ativos ocorre a mensagem: **Código do Plano não cadastrado**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33044003252375)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, normalmente devido a preenchimento de **Filial e/ou Mês e ano** nas tabelas correspondentes ao plano.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse **Atualizações/ Definições de Cálculo/ Manutenção de Tabelas**  
2. Para o Plano de Saúde, verifique a tabela S016 e para o Plano Odontológico, verifique a S017.  
No exemplo abaixo, o fornecedor com código 02 possui o campo **Mês/Ano** preenchido. Caso deseje informar esse plano para um período futuro, será necessário deixar esse campo **em branco.**  
Já para o fornecedor com código 01, o campo **Filial** está preenchido, o que significa que esse fornecedor estará disponível apenas para a filial 02. Se o fornecedor atender a todas as filiais, o campo deve permanecer **em branco.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33043973761047)

3. Ainda na rotina de Manutenção de Tabelas, verifique a tabela relacionada ao plano vinculado ao funcionário.  
No exemplo abaixo, utilizamos a tabela **S028 - Assistência Médica - Valor Fixo**. O plano com código 15 possui o campo **Mês/Ano** preenchido; caso deseje cadastrar esse plano para um período futuro, será necessário deixar esse campo **em branco.**  
Já o plano com código 16 tem o campo **Filial** preenchido, o que significa que ele estará disponível apenas para a filial 02. Se o plano for válido para todas as filiais, o campo deve permanecer **em branco.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33043973763863)

Para verificar em qual plano e tabela o funcionário está ou será cadastrado, consulte o campo **"Cód Plano"** na rotina de Planos Ativos.  
No exemplo abaixo, o funcionário será cadastrado na Assistência Médica com um plano do tipo Valor Fixo, correspondendo à tabela **S028**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33043973768471)

**Saiba Mais**[RH - Linha Protheus - GPE - Descontar plano de saúde do cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410634750743-RH-Linha-Protheus-GPE-Descontar-plano-de-sa%C3%BAde-do-c%C3%A1lculo-de-f%C3%A9rias?source=search)  
[RH - Linha Protheus - GPE - Cancelamento do Plano de Saúde/Odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050086373-RH-Linha-Protheus-GPE-Cancelamento-do-Plano-de-Sa%C3%BAde-Odontol%C3%B3gico?source=search)  
[RH - Linha Protheus - GPE - Transferência em Lote do Plano de Saúde/Odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042994494--RH-Linha-Protheus-GPE-Transfer%C3%AAncia-em-Lote-do-Plano-de-Sa%C3%BAde-Odontol%C3%B3gico?source=search)  
[RH - Linha Protheus - GPE - Cálculo do plano de saúde proporcional após encerramento do plano](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058213214-RH-Linha-Protheus-GPE-C%C3%A1lculo-do-plano-de-sa%C3%BAde-proporcional-ap%C3%B3s-encerramento-do-plano?source=search)
