---
article_id: 360056360933
category: RH - Soluções para error.log
content_hash: 05428b2f905b76ac45ccc6526792e2d816778bd8d76495b9b5261aae9e424ec3
fetched_at: '2026-06-28T22:44:08.928177+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Error log na conclusão de várias rotinas - type
  mismatch on / on FINSSEMP
type: support-article
updated_at: '2022-10-19T13:36:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056360933-RH-Linha-Protheus-GPE-Error-log-na-conclus%C3%A3o-de-v%C3%A1rias-rotinas-type-mismatch-on-on-FINSSEMP
---

**Ocorrência**Ao tentar concluir várias rotinas gera ***error log**: **"type mismatch on / on*** **FINSSEMP(GPEXCIMP.PRX)"****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - à partir da versão 12.1.17 **Causa**  
Devido a falta do tipo de contrato 1 e 2 nas tabelas S037 e S038 de Manutenção de Tabelas  
  
**Solução**Para correção seguir os passos abaixo  
**1.** Acessar o Sistema no Módulo de Gestão de Pessoal;  
**2.** Acessar a rotina de Atualizações/Definições de Cálculo/Manutenção de Tabelas;  
**3.** Acessar as Tabelas **S037** e **S038;  
4.** As tabelas devem constar os dois tipos de contrato para cada linha cadastrada, como exemplificado abaixo:  
  
Tabela - S037  
![](https://totvssuporte.zendesk.com/attachments/token/nhPnqVQrV51iUaUkpDlQdpUTB/?name=inline-1496500762.png)  
  
Tabela - S038  
![](https://totvssuporte.zendesk.com/attachments/token/eFAzyJkjJ2dvuTAd1YBmmBTWz/?name=inline1189602790.png)  
  
**Importante**Caso esteja com o campo “**Filial”** ou “**Mês/Ano**” preenchido, deverá constar os dois tipos de contrato para cada filial ou mês/ano.  
  
**Obs.:**  
Caso mesmo efetuando o procedimento acima o erro persista, é muito possível que a estrutura de suas tabelas estejam incorretas, portanto, peço que realize o procedimento informado abaixo, de:  
**1.** Faça um backup da sua tabela RCC;  
**2.** Acesse a tabela S037 e S038 pela rotina e delete todos os itens;  
**3.** Pela própria rotina, cadastre novas linhas referentes ao mês em questão.  
  
**Saiba mais:**  
Pacote acumulado RH: [MP - GPE - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
Pacote Acumulado e-Social: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234>
