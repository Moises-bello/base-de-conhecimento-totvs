---
article_id: 360023123011
category: RH - Folha de Pagamento
content_hash: 2e058e092255f423db593de328a2e4727ebac33870b0fc6eb2ac5ed65bcbc9f9
fetched_at: '2026-06-28T22:44:15.027260+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - INSS Múltiplos Vínculos
type: support-article
updated_at: '2025-09-23T11:45:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023123011-RH-Linha-Protheus-GPE-INSS-M%C3%BAltiplos-V%C3%ADnculos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22248432629911)** Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Configuração para cálculo de **INSS Múltiplos Vínculos**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**  
É permitido que um mesmo funcionário possua mais de um contrato de trabalho, o que se define como funcionário com Múltiplos Vínculos e que influencia no cálculo do INSS. O rateio de INSS somente terá efeito quando o **CPF** processado **possuir mais de uma matrícula com movimento.**  
  
Para tratamento do cálculo do INSS de funcionários com mais de um vínculo empregatício devem ser utilizados os seguintes identificadores:

|  |  |  |  |
| --- | --- | --- | --- |
| **Id** | **Descrição** | **Tipo Cod** | **Tipo** |
| 0236 | Base IR Férias Outros Períodos | Base Provento | Valor |
| 0237 | IR Férias Outros Períodos | Base Provento | Valor |
| 0288 | Salário Contribuição INSS Outras Empresas | Base Provento | Valor |
| 0289 | Desconto INSS Outras Empresas | Base Provento | Valor |
| 0290 | Base INSS 13º Outras Empresas | Base Provento | Valor |
| 0291 | INSS 13º Outras Empresas | Base Provento | Valor |
| 0396 | Base INSS Férias Outros Períodos | Base Provento | Valor |
| 0397 | INSS Férias Outros Períodos | Base Provento | Valor |
| 0992 | Base IR Outras Empresas | Base Provento | Valor |
| 0993 | IR Outras Empresas | Base Provento | Valor |
| 0994 | Base IR Outras Empresas 13º Salário | Base Provento | Valor |
| 0995 | IR Outras Empresas 13º Salário | Base Provento | Valor |
| 1847 | Base INSS Autônomo Outras Empresas | Base Provento | Valor |
| 1951 | Deduções modelo completo IR Folha no período anterior | Base Provento | Valor |

Consulte quais verbas estão cadastradas com os id's citados acima no cadastro de verbas **GPEA040**em **Atualizações > Definições de Cálculo > Verbas**

Execute o lançamento manual nestas verbas para o funcionário com o valor correspondente da base do INSS e valor descontado de INSS do funcionário na outra empresa disponível em Gestão Pessoal > Atualizações > Lançamento >  Por Funcionário - Rotina **GPEA090**.  
  
Após este lançamento, calcule a folha, onde o sistema fará a proporção do que já foi descontado e da tabela de INSS, apurando se haverá desconto da diferença entre o Teto e o descontado em uma das empresas ou se já foi recolhido o teto na outra empresa  
  
**Saiba Mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)

[RH - Linha Protheus - GPE - Como configurar o cálculo de múltiplos vínculos na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027693112-RH-Linha-Protheus-GPE-Como-configurar-o-c%C3%A1lculo-de-m%C3%BAltiplos-v%C3%ADnculos-na-vers%C3%A3o-12)

[RH - Linha Protheus - GPE - No Dissídio Retroativo, Sistema não considera valor de INSS já reajustado nos vínculos Anteriores](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052624413-RH-Linha-Protheus-GPE-No-Diss%C3%ADdio-Retroativo-Sistema-n%C3%A3o-considera-valor-de-INSS-j%C3%A1-reajustado-nos-v%C3%ADnculos-Anteriores)
