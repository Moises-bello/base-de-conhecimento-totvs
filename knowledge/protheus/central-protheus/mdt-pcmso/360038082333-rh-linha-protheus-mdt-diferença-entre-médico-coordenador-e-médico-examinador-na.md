---
article_id: 360038082333
category: MDT - PCMSO
content_hash: 5dcae6ecf5926f5b2931f04dd77718d70acff32fee19aba2efa2b810ec23cc38
fetched_at: '2026-06-28T22:44:28.430315+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Diferença entre Médico Coordenador e Médico  Examinador
  na emissão do ASO Atestado de Saúde Ocupacional
type: support-article
updated_at: '2025-09-03T13:51:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038082333-RH-Linha-Protheus-MDT-Diferen%C3%A7a-entre-M%C3%A9dico-Coordenador-e-M%C3%A9dico-Examinador-na-emiss%C3%A3o-do-ASO-Atestado-de-Sa%C3%BAde-Ocupacional
---

**Dúvida**Qual a diferença entre o Médico Coordenador e Médico Examinador na emissão do **(ASO)** Atestado de Saúde Ocupacional ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança – Todas as versões  
  
**Solução**Para gerar as informações do Médico Coordenador do **ASO**o sistema utiliza a referencia abaixo:  
TMW - Parâmetros do PCMSO - Médico Coordenador  
  
Quando  é realizado uma  **Programação de exames**, o sistema utiliza o **Médico Responsável** pela programação para gerar as informações no aso.  
  
No que se refere ao **Médico Examinador** as informações que são registradas na emissão do **ASO**.  
TMY - Dados do Atestado ( data, medico, parecer etc..)  
O médico que realizou o exame atestado aso.

1. Para definir o **médico coordenador**o relatório primeiramente recolhe a informação referente a data de geração do ASO (**TMY\_DTGERA**).
2. Com essa informação é percorrida a tabela de Parâmetros do PCMSO (**TMW**) verificando se esta data corresponde ao período de vigência de alguma programação. Período este definido através do intervalo formado entre as datas de início (**TMW\_DTINIC**) e fim (**TMW\_DTFIM**) do PCMSO.
3. Assim que o relatório encontrar uma programação correspondente a data de geração do ASO será recolhido o código do médico responsável naquele período específico (**TMW\_CODUSU**). Com este código definido, o relatório "tem conhecimento" de qual médico foi apontado como responsável naquele período e com isso realiza a impressão do nome do mesmo como o **Coordenador** no atestado.

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
