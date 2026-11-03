---
article_id: 5223165502359
category: PONTO ELETRÔNICO
content_hash: 14c6039dbc7abbc4ca2fb9f52531a0962a1c05807848321c44504e6f676502ee
fetched_at: '2026-06-28T22:44:36.664911+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como verificar o espelho de ponto em período
  futuro
type: support-article
updated_at: '2026-01-20T12:30:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5223165502359-RH-Linha-Protheus-MEU-RH-Como-verificar-o-espelho-de-ponto-em-per%C3%ADodo-futuro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27489298874135) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como verificar o espelho de ponto em período futuro?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - todas as versões  
  
**Solução**  
Com a criação do parâmetro **MV\_MRHDPER**, hoje é possível visualizar o espelho de ponto em período futuro de acordo com o seu conteúdo definido neste parâmetro.  
  
Para o correto funcionamento da rotina, este parâmetro que é numérico irá somar a quantidade de dias a data final do período atual, isso de acordo com o conteúdo do parâmetro **MV\_PONMES**, para que o **próximo período** esteja disponível para visualização.  
  
**Obs.:** Este parâmetro somente conseguirá projetar o período cuja data atual do sistema esteja compreendida, ou seja, para o correto funcionamento deste parâmetro, não pode existir dois períodos anteriores de Apontamento. **Ex.:** Se o Período de Apontamento for entre **01/01/2022** **à** **31/01/2022** e tentar acessar no dia **01/03/2022**, **será projetado** o Período de **01/03/2022** **à** **31/03/2022** e **não** mais o período **01/02/2022 à 28/02/2022**.  
  
**Exemplo:**  
**- MV\_PONMES = 20220101/20220131**  
**- MV\_MRHDPER = 3**  
**- Data Fim do Período conforme MV\_PONMES = 31/01/2022**  
**- Data Projetada = 31/01/2022 + 3 Dias = 03/02/2022**  
  
Logo, o **próximo** período somente estará disponível para visualização no dia **03/02/2022** ou após este dia.  
  
Caso o funcionário acesse o Meu RH no dia 01/02 ou 02/02/2022, continuará vendo o período conforme o MV\_PONMES, ou seja, de 01/01 a 31/01/2022.  
  
**OBS:** Caso o parâmetro não exista, ou seu conteúdo seja igual a 0, o próximo período nunca será visualizado.

|  |  |
| --- | --- |
| **Nome da Variável** | **MV\_MRHDPER** |
| **Tipo** | Numérico |
| **Descrição** | Informar o número de dias a serem somados à data final do período do ponto (conforme MV\_PONMES), para liberação do próximo período. |
| **Valor Padrão** | 0 |

**Informação Importante:**Esta implementação **NÃO ALTERARÁ** o conteúdo dos parâmetros MV\_PONMES e MV\_PAPONTA, mas apenas **PROJETARÁ** um novo período de ponto, conforme os dias existentes no período atual  
  
**Impactos dessa nova funcionalidade:**  
1 - Caso o funcionário acesse o período futuro, o Meu RH se comportará da seguinte forma.  
  
1.1 - No dashboard, o banco de horas do funcionário e o banco de horas do time serão apurados conforme o novo período.  
![ZMypE5seaK.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5227228101783)  
  
1.2 - O banco de horas do espelho de ponto, bem como o resumo do período, serão apurados conforme o período projetado.  
  
1.3 - Será possível realizar o download do espelho do período projetado.  
  
1.4 - O resumo diário também será apurado conforme o dia escolhido, seja do período atual ou projetado  
  
1.5 - Será possível incluir/excluir/alterar batidas do período projetado.  
![yZl2vCgcNh.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5227087624983)  
  
**Saiba Mais**  
[**Espelho de ponto em período futuro**](https://tdn.engpro.totvs.com.br/pages/viewpage.action?pageId=663593191)  
[**CLIQUE AQUI**para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI**para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
