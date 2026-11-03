---
article_id: 38603473949591
category: RH - Folha de Pagamento
content_hash: 742a06739e0518baf42d9631096d410ef9a3e53ccca0531f67b88cfeb21b81f2
fetched_at: '2026-06-28T22:44:16.402138+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Valor da verba de líquido da folha diferente do
  líquido apresentado no relatório da Folha de Pagamento
type: support-article
updated_at: '2026-02-24T14:20:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38603473949591-RH-Linha-Protheus-GPE-Valor-da-verba-de-l%C3%ADquido-da-folha-diferente-do-l%C3%ADquido-apresentado-no-relat%C3%B3rio-da-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38603481555991) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao gerar o relatório de Folha de Pagamento, o valor de líquido apresentado está diferente do valor demonstrado na verba de líquido.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da Versão 12  
  
**Causa**  
Esse incidente ocorre, quando a verba de id **0166 - DSR Sobre Comissões** - esta lançada na **RGB (Atualizações  >Lançamentos > Por Funcionário)** com origem **G- Gerada**.  
  
**Solução**  
Para solucionar essa ocorrência, será necessário **atualizar** o Sistema com a última **Expedição Contínua do RH** e **Lib**, pois foi feito ajuste no cálculo da folha para considerar corretamente o lançamento de DSR sobre comissão, garantindo o cálculo correto do valor líquido.

**Expedição Contínua**

<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO_CONTINUA>

**LIB**

Até a versão 12.1.2310: <https://suporte.totvs.com/portal/p/10098/download?e=1050526>

A partir da versão 12.1.2410: <https://suporte.totvs.com/portal/p/10098/download?e=1168735>

**Saiba Mais**

[Verba de líquido da folha é calculada errada quando a verba de id 0166 esta lançada na RGB com origem G](https://tdn.totvs.com/pages/viewpage.action?pageId=1019325564)

[RH - Linha Protheus - GPE - Referencias e valores duplicados no Relatório Personalizado GPER106](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024820033-RH-Linha-Protheus-GPE-Referencias-e-valores-duplicados-no-Relat%C3%B3rio-Personalizado-GPER106)

[RH - Linha Protheus - GPE - Quais relatórios demonstram os valores da folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10091236988567-RH-Linha-Protheus-GPE-Quais-relat%C3%B3rios-demonstram-os-valores-da-folha-de-pagamento)

[RH - Linha Protheus - GPE - Quais relatórios periódicos são gerados em planilha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055157993-RH-Linha-Protheus-GPE-Quais-relat%C3%B3rios-peri%C3%B3dicos-s%C3%A3o-gerados-em-planilha)
