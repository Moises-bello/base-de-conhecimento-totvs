---
article_id: 360015970332
category: RH - Rescisão
content_hash: 860f1c4f88c068b61c484e2dc2b4af694f75a22ea3f69986c15c5d4180d740da
fetched_at: '2026-06-28T22:43:48.340781+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Como calcular rescisão de um estagiário
type: support-article
updated_at: '2025-09-10T17:16:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015970332-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-de-um-estagi%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34843646430359) Tempo aproximado para leitura:** **00:02:00 min****Dúvida**Como calcular rescisão de um estagiário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Para realizar o cálculo da rescisão de um Estagiário, favor seguir os seguintes passos:

1. Cadastre as verbas com Id de cálculo 1424, 1425, 0891, 0219 na rotina Verbas pelo caminho Atualizações/Definições de cálculo/Verbas:  
![](https://totvssuporte.zendesk.com/attachments/token/vdnuoG3sZNuBdhTzEg0JDH0j1/?name=inline-1378746606.png)  
![](https://totvssuporte.zendesk.com/attachments/token/e30swC1veD0Xnso545NyucuV8/?name=inline1210759543.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/eDxAzvGrrVjj2ghFzpk6ETmN5/?name=inline1176626760.png)  
![](https://totvssuporte.zendesk.com/attachments/token/fRR1qSLIPx0v55YsgB3eipcpl/?name=inline100425281.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/qbxqRprWUbVFu2ZwWjcCHjotq/?name=inline-1274812905.png)  
![](https://totvssuporte.zendesk.com/attachments/token/JCc2Gr4g2vs9F83IoSEv9TWcp/?name=inline-474439622.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/EYMX1z4jCHiNSGiJWpgcGvjnr/?name=inline-289292958.png)  
![](https://totvssuporte.zendesk.com/attachments/token/k6gRoPCDQ9Sj49sHMLfdou7cy/?name=inline-116578160.png)

2. Cadastre um novo código homolognet na Tabela S019 pelo caminho Atualizações/Definições de cálculo/Manutenção de tabelas-S019:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10468073819159)

3. Cadastre o Tipo de Rescisão na Tabela S043 pelo caminho Atualizações/Definições de cálculo/Manutenção de tabelas-S043:  
![](https://totvssuporte.zendesk.com/attachments/token/y4tsp3dhEuOxvkoEzczQEVSYl/?name=inline-893169481.png)  
![](https://totvssuporte.zendesk.com/attachments/token/H57yMHJnU0F5wrqbP6g6E3puO/?name=inline-1304184062.png)  
  
4. Confirma o cadastro do estagiário na rotina Funcionários pelo caminho Atualizações/Funcionários/Funcionário:  
![](https://totvssuporte.zendesk.com/attachments/token/calhrfkoHQynztxP5JOkxYtA7/?name=inline75806433.png)  
  
5. Inclua o roteiro RES no cadastro de Períodos pelo caminho Atualizações/Definições de cálculo/Períodos:  
![](https://totvssuporte.zendesk.com/attachments/token/X9NOrDIB21OFy65HTDTgIeZF9/?name=inline2049054937.png)  
  
6. Confira se tem o período de recesso cadastrado no Controle Dias de Direito pelo caminho Atualizações/Funcionários/Controle dias de Direito:  
\*Férias vencidas e proporcionais.  
\*Verba com Id 0891.  
![](https://totvssuporte.zendesk.com/attachments/token/MCPZLsVlRfGzmFtuP6BdMo05u/?name=inline194909921.png)  
  
7. Calcule a rescisão pelo caminho Miscelânea/Cálculos/Rescisões:  
![](https://totvssuporte.zendesk.com/attachments/token/0o9kZxn8UZhi3r0vwpChwChOr/?name=inline1581805080.png)

**Observação:**O Protheus não possui um tratamento padrão para a execução do cálculo da rescisão de estágio, uma vez que tal não possui vínculo empregatício e embasamento jurídico.

Sendo assim, este documento demonstra a possibilidade do cliente executar o procedimento para atender a sua necessidade.

Salientamos também que estagiário não possui incidência em suas verbas, portanto, a Totvs não se responsabilizará pela geração de verbas incorretas no cálculo da rescisão.

**IMPORTANTE**  
Em casos de rescisão para estagiários após o cálculo do 13º salário, 2º parcela ou parcela única, se não houver nenhuma verba que gere diferenças de 13º salário e que possuam incidência para IRRF e Ref a 13º, o sistema não irá apresentar a verba de IRRF sobre 13º.

Entendemos que da forma que o sistema esta apresentando os cálculos na rescisão esta corretos, pois não gera divergências no pagamento de impostos e nem na geração das verbas ao eSocial.

**Saiba Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
