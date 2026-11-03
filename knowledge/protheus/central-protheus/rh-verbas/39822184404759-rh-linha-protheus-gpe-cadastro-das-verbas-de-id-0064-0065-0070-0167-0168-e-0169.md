---
article_id: 39822184404759
category: 'RH - Verbas '
content_hash: f3534dc36f527ed152c4e8619fe5386e4cbb1108fddf4c9fb335508e28e33f6b
fetched_at: '2026-06-28T22:43:19.880430+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro das verbas de id 0064, 0065, 0070, 0167,
  0168 e 0169
type: support-article
updated_at: '2026-05-26T18:52:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39822184404759-RH-Linha-Protheus-GPE-Cadastro-das-verbas-de-id-0064-0065-0070-0167-0168-e-0169
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39822200087191) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Cadastro das verbas de id 0064, 0065, 0070, 0167, 0168 e 0169  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
  
**1º Cenário:** A verba de ID 0168 está com SIM para IR.

Configurar o campo RV\_INCIRF = 09 da verba com ID 0065 - INSS sobre Férias  
Configurar o campo RV\_INCIRF = 43 da verba com ID 0168 - Dedução do INSS sobre B.C. IRRF s/ Férias  
Não é necessário alterar a configuração do campo RV\_IR.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39822184378263)

**2º Cenário:** As verbas de ID 0167, 0168 e 0169 estão com NÃO para IRRF, e as verbas de ID 0064, 0065, 0070 estão com SIM para IR.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39822184379927)

**Para 2026 a verba de id 0065 e 0168** devem seguir suas parametrizações conforme boletim abaixo, onde as verbas originais com idnecificador ficarão com incidencia 9 e somente as verbas substitutas terão incidencia de IRRF. Lembrando que somente deve ser parametrizado para o esocial um id ou o 0065 ou o 0168, pois ambos possuem as mesmas informações:  
[RH - Linha Protheus - GPE - eSocial - S-5001 - Valores de INSS de férias e Dedução de INSS na base de IRRF férias duplicados após criação de verbas de substituição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38333029992087-RH-Linha-Protheus-GPE-eSocial-S-5001-S-5002-Valores-de-INSS-de-f%C3%A9rias-e-Dedu%C3%A7%C3%A3o-de-INSS-na-base-de-IRRF-f%C3%A9rias-duplicados-ap%C3%B3s-cria%C3%A7%C3%A3o-de-verbas-de-substitui%C3%A7%C3%A3o)

**Saiba Mais**  
[Incidências de Verbas para a DIRF - SUGESTÃO DE PREENCHIMENTO](https://tdn.totvs.com/pages/viewpage.action?pageId=706926617)
