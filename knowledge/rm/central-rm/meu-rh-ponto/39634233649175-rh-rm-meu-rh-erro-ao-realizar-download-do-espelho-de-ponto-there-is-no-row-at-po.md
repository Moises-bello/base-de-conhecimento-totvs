---
article_id: 39634233649175
category: Meu RH - Ponto
content_hash: 987897aa73347170cb0327f6871ccabf5fe0ae656b7d6a5b96c4bb8bdd9d1128
fetched_at: '2026-06-28T22:47:30.230703+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Erro ao realizar download do espelho de ponto "There is
  no row at position 0"
type: support-article
updated_at: '2026-04-10T13:12:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39634233649175-RH-RM-Meu-RH-Erro-ao-realizar-download-do-espelho-de-ponto-There-is-no-row-at-position-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39634275286295) Tempo aproximado para leitura: **00:02:15 min**  
  
**Ocorrência**  
Ao realizar o download do relatório espelho de ponto no Meu RH, é apresentado a mensagem de erro: "There is no row at position 0".  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39634233630999)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas Versões

**Causa**  
Esse erro ocorre, quando a parametrização do download do espelho de ponto para o Meu RH está incompleta ou incorreta.  
  
**Solução**  
Para que o download do espelho de ponto funcione corretamente, é necessário realizar as seguintes validações:

1. **Parametrização do relatório no grupo de quiosque**  
   O relatório deve estar vinculado ao grupo de quiosque associado aos funcionários, no seguinte caminho:  
   **Automação de Ponto | Configurações | Parametrizador | RM Portal | Espelho Funcionário | Código do Relatório**

   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39634275287831)

2. **Configuração do tipo do relatório**  
   Para que o relatório seja listado no campo **"Código do Relatório"**, é necessário que, em sua estrutura acessada através do caminho **Gestão | RM Reports**, o campo **Tipo** esteja configurado como **181 - Espelho do Cartão de Ponto.**  
   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39634233632151)
3. **Criação do perfil de parâmetros**  
   Após vincular o relatório, é necessário criar um perfil de parâmetros com o nome **"MeuRH"**, contendo os parâmetros desejados. Esse perfil será utilizado na geração do relatório pelo app Meu RH, no caminho: **Automação de Ponto | Relatórios | Espelho do Cartão**  
   **![](https://totvssuporte.zendesk.com/attachments/token/E5mS1ktMYZT8OwU5vE0X3jHAX/?name=inline1601044054.png)**  
   **![](https://p23.zdusercontent.com/attachment/888110/Y3DogPP09j99thmnJMI2zg0o3?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..JSinnmGzqVs_TjpQmTx61w.sJN6Xp5dTwCR1-T00JH_xengmtiK7I8kRoLbD9pSBtZkJ1rh_EqBIMOimbQbZxTE6map-W_7N-uwlJKlO7BGZdLx_9YIcYJSjYcZrXO0Dy98kpXMGT3ZZHGfcQh4F5tI6a1t0wxCHgF2F3dftm2zRQLopKqHHVLj01p3Ug_opnJmJTb_tc271SL9YeTvdrFPwDX1iX247UvF2JUypASCPliuxnaeQ70UHLPc679cWdM6MOid7GyqitvR8MxNmzL4TgB_woIeNsTWLwZYdK8GuSHLOQYN2D-e1IoDOuHv9wA.2sXxSE549BHg2lQ9iGK2pw)**

Após realizar essas configurações, o relatório deverá ser gerado corretamente no Meu RH, sem a ocorrência do erro informado.

**Importante:** Caso o erro persista, o problema pode estar relacionado ao relatório utilizado. Neste cenário, recomendamos que acesse o [**TOTVS Compartilhamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8876331402775-Framework-Linha-RM-Frame-TOTVS-Compartilhamento) e faça o download novamente do relatório padrão código "**PTOREL 01.0001"** e durante a importação, marque a opção **"Sobrescrever Existente".** Após reimportar, é necessário atualizar o Grupo de Quiosque novamente, vinculando o novo relatório em "**Código do Relatório".**

**Saiba Mais:**  
[**RH - RM - Meu RH - Como habilitar o download do espelho de ponto no Meu RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10759355849367-RH-RM-Meu-RH-Como-habilitar-o-download-do-espelho-de-ponto-no-Meu-RH#:~:text=Como%20habilitar%20o%20download%20do%20espelho%20de%20ponto%20no%20Meu%20RH%3F&text=Acesse%20Servi%C3%A7os%20Globais%20%7C%20Seguran%C3%A7a%20%7C%20Perfis,Ponto%20e%20permita%20o%20acesso.)
