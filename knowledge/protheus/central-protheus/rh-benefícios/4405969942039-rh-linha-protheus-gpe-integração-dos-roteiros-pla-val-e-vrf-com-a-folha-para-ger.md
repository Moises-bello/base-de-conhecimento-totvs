---
article_id: 4405969942039
category: RH - Benefícios
content_hash: 843629f60c11b96a32a29e8ef5a818a9d9ebbc17b2b82f44bb743d47088b248d
fetched_at: '2026-06-28T22:44:04.897479+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Integração dos roteiros PLA, VAL e VRF com a Folha
  para gerar o valor total do benefício conforme determinação do MOS da versão S-1.0
type: support-article
updated_at: '2025-09-30T11:32:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405969942039-RH-Linha-Protheus-GPE-Integra%C3%A7%C3%A3o-dos-roteiros-PLA-VAL-e-VRF-com-a-Folha-para-gerar-o-valor-total-do-benef%C3%ADcio-conforme-determina%C3%A7%C3%A3o-do-MOS-da-vers%C3%A3o-S-1-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32576716466071) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Ajuste realizado na integração dos roteiros PLA, VAL e VRF com a Folha para gerar o valor total do benefício conforme determinação do MOS da versão S-1.0.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No **MOS da versão S-1.0,** disponível [aqui](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-0-consolidada-ate-a-no-s-1-0-04-2021.pdf), **há o seguinte trecho na página 78:** Valores relacionados a **parcelas in natura:**  
**8.1.** Os valores de parcelas salariais in natura, a exemplo das informadas em rubricas atreladas às naturezas 1010 - Salário in natura - Pagos em bens ou serviços, 1806 - Alimentação em ticket ou cartão, vinculada ao PAT, 1807 - Alimentação em ticket ou cartão, não vinculada ao PAT, 1808 - Cesta básica  
ou refeição, vinculada ao PAT, 1809 - Cesta básica ou refeição, não vinculada ao PAT, 2902 - Vestuário e equipamentos, 9910 - Seguros ou 9911 - Assistência Médica devem ser informados pelo valor total e não apenas em relação à parte custeada pelo empregador. Exemplos:  
  
1) se o declarante cadastrado no PAT fornece cartão alimentação de R$ 200,00 e desconta o correspondente a R$ 30,00 do empregado, deve informar o valor de R$ 200,00 em rubrica atrelada a natureza 1806 e o desconto de R$ 30,00 em rubrica atrelada a natureza 9241.  
2) se o declarante contrata apólice de seguro beneficiando seus empregados e cujo valor mensal corresponde a R$ 80,00, sem que seja feito quaisquer descontos de seus empregados, deve informar o valor de R$ 80,00 em rubrica atrelada à natureza 9910.  
3) se o declarante fornece vale transporte ao seu empregado, no valor R$ 200,00 mensais e desconta R$ 70,00 do empregado relativo a esses vales, deve informar o valor de R$ 200,00 em rubrica atrelada à natureza 1810 e R$ 70,00 em rubrica atrelada à natureza 9216.

Segue **detalhamento da geração das verbas referente ao valor total ao efetuar integração com a Folha por roteiro.**

* [Roteiro BEN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14630329010967-RH-Linha-Protheus-GPE-Valor-total-do-benef%C3%ADcio-calculado-no-Roteiro-BEN-conforme-determina%C3%A7%C3%A3o-do-MOS-da-vers%C3%A3o-S-1-0)
* [Roteiro VRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14597169300503-RH-Linha-Protheus-GPE-Valor-total-do-benef%C3%ADcio-de-vale-refei%C3%A7%C3%A3o-conforme-determina%C3%A7%C3%A3o-do-MOS-da-vers%C3%A3o-S-1-0)
* [Roteiro VAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14597581804823-RH-Linha-Protheus-GPE-Valor-total-do-benef%C3%ADcio-de-vale-alimenta%C3%A7%C3%A3o-conforme-determina%C3%A7%C3%A3o-do-MOS-da-vers%C3%A3o-S-1-0)
* [Roteiro VTR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14597024778519-RH-Linha-Protheus-GPE-Valor-total-do-benef%C3%ADcio-de-vale-transporte-conforme-determina%C3%A7%C3%A3o-do-MOS-da-vers%C3%A3o-S-1-0)
* [Roteiro PLA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14651517808407-RH-Linha-Protheus-GPE-Valor-total-do-benef%C3%ADcio-de-assist%C3%AAncia-m%C3%A9dica-conforme-determina%C3%A7%C3%A3o-do-MOS-da-vers%C3%A3o-S-1-0)

**Consulte a** [documentação técnica.](https://tdn.totvs.com/pages/releaseview.action?pageId=630365963#beneficios-BEN) **Observação:  
Não houve alteração no cálculo dos benefícios.** Foram criados os IDs de cálculo 1862 a 1868, que não são obrigatórios. Apenas deve-se cadastrar verbas vinculadas a esses IDs se houver necessidade.
