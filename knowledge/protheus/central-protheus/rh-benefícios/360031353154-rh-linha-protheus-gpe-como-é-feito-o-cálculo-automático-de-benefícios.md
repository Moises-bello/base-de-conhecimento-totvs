---
article_id: 360031353154
category: RH - Benefícios
content_hash: 7ce08b7c500b192da1579ec5743bbf1191b6ec7c0e740ef585be09f184b657b4
fetched_at: '2026-06-28T22:44:03.765856+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como é feito o Cálculo Automático de Benefícios
type: support-article
updated_at: '2025-10-15T17:56:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031353154-RH-Linha-Protheus-GPE-Como-%C3%A9-feito-o-C%C3%A1lculo-Autom%C3%A1tico-de-Benef%C3%ADcios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33789607129879)** Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como é feito o Cálculo Automático de Benefícios?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
O  Cálculo Automático de Benefícios permite **vincular os benefícios à outras entidades** e não necessariamente ao funcionário, possibilitando calcular um mesmo benefício para todos os funcionários de determinada filial, por exemplo.  
Para que o sistema consiga realizar o cálculo, é necessário **definir uma ordem de prioridade para as entidades escolhidas.** Definida a ordem, basta vincular os benefícios às entidades e executar o cálculo.  
  
Segue abaixo um passo a passo do processo:  
  
**1**. Deixe o conteúdo do parâmetro **MV\_CALCBEN=.T.**  
  
**2**. Cadastre um **Critério** com a ordem de busca que o sistema deverá seguir para cálculo através do menu **Atualizações > Benefícios > Cálculo Automático > Critérios de Benefícios:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042204134)

**3**. Vincule os benefícios a cada critério na rotina **Lançamento de Vínculos** através do menu **Atualizações > Benefícios > Cálculo Automático > Lançamento de Vínculos >** clique sobre o critério que deseja configurar > **Manutenção.** Neste exemplo, será utilizado o **Sindicato:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084898613)

**4**. Posicione o cursor em cima do **Tipo de Benefício** desejado e preencha o *grid* inferior com:  
- Código de Sindicato que pertence o benefício  
- Código do Benefício que será vinculado  
- Data inicial de vigência deste critério  
- Data final (se houver)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33993898453015)  
  
  
  
Outros exemplos:  
**- Vale Cultura** vinculado à Filial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33993893350167)  
  
  
- **Subsídio Acadêmico** vinculado diretamente ao Funcionário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33993898459927)  
  
  
Em um exemplo prático, vamos supor que houve uma **alteração de Sindicato** vinculado ao Funcionário no dia 20.07, com isso, o resultado após o Cálculo Automático foi:  
- dois registros incluídos na tabela SM7 sendo um para cada benefício, e com o campo **Tipo de Cálculo = Automático**  
- **valores calculados proporcionalmente** aos dias que o Funcionário permaneceu em cada Sindicato durante o período.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33993898461335)  
  
  
Após o cálculo do roteiro de Outros Benefícios - BEN, também foram gerados dois registros, sendo:  
- um registro para o **Vale Cultura** definido por Filial e com o campo Tipo de Cálculo = Automático  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33993893355671)  
  
  
- um registro para o **Subsídio Acadêmico** com o campo Tipo de Cálculo = Informado, pois este foi vinculado diretamente ao Funcionário  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33993898463383)  
  
  
  
**Importante**  
• Para cálculos que possuem **integração com o SIGATEC - Gestão de Serviços**, é necessário deixar o parâmetro **MV\_TECXRH com .T.**  
**•** Quando habilitado, as entidades do Gestão de Serviços, SA1, ABS e TDX, são abertas apenas para visualização nesta tela. As alterações dos benefícios vinculados a essas entidades devem ser realizadas utilizando o módulo SIGATEC  
• O que define se o cálculo automático será ou não utilizado é o **Cadastro de Critério,** portanto, se **existir um critério ativo** para a filial e período informados no cálculo, o sistema irá buscar os benefícios vinculados a cada entidade  
• O cálculo automático busca as informações de transferências e alterações no cadastro do funcionário para determinar os benefícios e os dias que o funcionário tem direito.  
• Não é possível utilizar o cadastro de vale transporte na rotina de critério de benefícios, logo, não é possível realizar o cálculo automático para o roteiro VTR.

**Saiba Mais:**  
[Cálculo Automático de Benefícios](https://tdn.totvs.com/pages/releaseview.action?pageId=557350063)  
[RH - Linha Protheus - GPE - Como funciona a hierarquia do cálculo automático de benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiCe7rUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTI3NjY3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mdW5jaW9uYS1hLWhpZXJhcnF1aWEtZG8tYyVDMyVBMWxjdWxvLWF1dG9tJUMzJUExdGljby1kZS1iZW5lZiVDMyVBRGNpb3MGOwhUOg5zZWFyY2hfaWRJIik0NDk5MGQzMS01MzYyLTQzZDQtYjI5Ny0xNzcyMDg5YWI3ZGMGOwhGOglyYW5raQs6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhdjYWxjdWxvIGF1dG9tYXRpY28GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--bcdb8e3333182e0bd025203f7b29b6c4159b9e5f)  
[RH - Linha Protheus - GPE - Relatório de Conferência para Cálculo de Benefícios Automáticos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj6I8fUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBtGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjEwNjIzNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUmVsYXQlQzMlQjNyaW8tZGUtQ29uZmVyJUMzJUFBbmNpYS1wYXJhLUMlQzMlQTFsY3Vsby1kZS1CZW5lZiVDMyVBRGNpb3MtQXV0b20lQzMlQTF0aWNvcwY7CFQ6DnNlYXJjaF9pZEkiKWU3YTk5ZDZiLWYwOGEtNGI5OS04YmIzLTMxMTA4ODE5ZTdkZAY7CEY6CXJhbmtpCToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiJWNhbGN1bG8gYXV0b21hdGljbyBkZSBiZW5lZmljaW9zBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--cec72f7e5aa962b73ac108505a3f973fc3bbef6b)  
[RH - Linha Protheus - GPE - No cálculo automático de benefícios, o sistema faz o cálculo normalmente mesmo que não haja vínculo para receber benefício.](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiRCsbUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB%2BWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjAzNDE5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTm8tYyVDMyVBMWxjdWxvLWF1dG9tJUMzJUExdGljby1kZS1iZW5lZiVDMyVBRGNpb3Mtby1zaXN0ZW1hLWZhei1vLWMlQzMlQTFsY3Vsby1ub3JtYWxtZW50ZS1tZXNtby1xdWUtbiVDMyVBM28taGFqYS12JUMzJUFEbmN1bG8tcGFyYS1yZWNlYmVyLWJlbmVmJUMzJUFEY2lvLQY7CFQ6DnNlYXJjaF9pZEkiKTQ0OTkwZDMxLTUzNjItNDNkNC1iMjk3LTE3NzIwODlhYjdkYwY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiF2NhbGN1bG8gYXV0b21hdGljbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--55c3dba585e523420552e398ee64bc0026add67f)
