---
article_id: 36225327609751
category: RH - Folha de Pagamento
content_hash: 506a5789045915ba77289d93edb6b2333cf78b372cd506b738d390ffcd9a12d0
fetched_at: '2026-06-28T22:44:12.082747+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de horas extras não considera adicionais
  sobre sobre verbas na base de cálculo
type: support-article
updated_at: '2025-11-10T18:41:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36225327609751-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-horas-extras-n%C3%A3o-considera-adicionais-sobre-sobre-verbas-na-base-de-c%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36225353187351) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Cálculo de horas extras não considera adicionais sobre sobre verbas na base de cálculo.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) GPE - Gestão de Pessoal - Todas as versões

**Causa**  
Esse incidente ocorre, pois a **lógica do roteiro de cálculo** determina que as horas extras serão calculadas antes dos adicionais sobre verbas.  
  
1º Salário  
2º Adicionais sobre salário  
3º Valorização de HE, seguido dos Adicionais sobre salário + Verbas  
  
Por conta dessa ordenação, **não é possível** que o valor do adicional sobre verbas  seja incorporado na base da Hora Extra, visto que a HE é calculada antes do adicional.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o **SIGAGPE > Atualizações > Definições de Cálculo > Roteiros de Cálculo**;
2. Localize o roteiro de cálculo **FOL**;
3. Mova a fórmula responsável pelo adicional de periculosidade sobre verbas (**S\_CALCPERV**) ou pelo adicional de insalubridade sobre verbas (**S\_CALINSALV)** para ser executada **antes** da valorização das horas extras (antes da fórmula **S\_CALCVALO**);
4. **Desative** a fórmula da posição **original** no roteiro para evitar conflitos no cálculo (**Habilitado = Não**);

**Importante**  
Essa alteração **não é recomendada,**pois se houver alguma HE que deveria entrar para base do adicional ela não irá entrar, pelo mesmo motivo que o adicional não entra na base da HE no modelo atual, não estará calculada.  
Se não existem verbas que componham a base do adicional, não haverá problemas, mas o correto seria cadastrar o adicional com base no salário apenas.  
  
As alterações no roteiro de cálculo são consideradas customizações, portanto, a equipe de suporte N1 não fornece assistência nesse tipo de ajuste.  
  
**Saiba Mais**

[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
