---
article_id: 360026673572
category: TAF - REINF
content_hash: 579010645e0272d2dae27f873351198bc77afbfedd453133da45ccb3479ddd80
fetched_at: '2026-06-28T22:41:33.611709+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Atualização Completa
  Reinf
type: support-article
updated_at: '2026-03-17T13:23:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-Reinf
---

**Dúvida**

Como atualizar o TAF para geração da Reinf?

**Produto**

TAF - SIGATAF - A partir da 12.1.27

**Solução**

Atualmente existe duas formas de atualizar o TAF:

- Aplicando patch e rodando UPDDISTR, nas versões recentes do TAF. (independente se for segregado ou não)

- Utilizando o TAF Atualizador com o TAF Segregado (Clientes que utilizam RM, Logix, Datasul e outros)

Caso a release do TAF Segregado seja igual ou superior a 12.1.33, deve ser efetuada a forma de atualizar (aplicando patch + UPDDISTR) sem a necessidade de utilizar o TAF Atualizador. 

Segue procedimento abaixo:

Parâmetro **MV\_TAFVLRE** precisa estar com o conteúdo 2\_01\_02 para ambiente em

Produção.

* [TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233-TAF-CONFIGURADOR-Como-acessar-os-par%C3%A2metros-do-sistema-?source=search)

***1 - TAF Segregado release inferior a 12.1.33 e 12.1.2210***

Acessar no TAF a rotina diagnóstico; caso a release do TAF Segregado inferior à release 12.1.27:

[Automação Fiscal - CONFIGURAÇÃO - Como acessar a tela de diagnósticos no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002485641-Automa%C3%A7%C3%A3o-Fiscal-CONFIGURA%C3%87%C3%83O-Como-acessar-a-tela-de-diagn%C3%B3sticos-no-TAF)

Efetue o download do atualizador.

<https://suporte.totvs.com/portal/p/10098/download#detail/695524>

E Siga a documentação do Link:

[TAF - ATUALIZAÇÃO - Como atualizar o TAF e o TSS via atualizador? (SEGREGADO)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020127812-TAF-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TAF-e-o-TSS-via-atualizador-SEGREGADO-?source=search)

**IMPORTANTE: Certifique-se de que o seu banco de dados é homologado para o produto, dúvidas relacionadas à compatibilidade, contatar time de tecnologia e atendimento para maiores esclarecimentos.**

<https://tdn.totvs.com/display/tec/DBAccess+-+Banco+de+dados>

***2 - Pacote TAF:***

**Release:**

**12.1.2310:** <https://suporte.totvs.com/portal/p/10098/download#detail/1126399>

**12.1.2410:** <https://suporte.totvs.com/portal/p/10098/download?e=1174332>

**12.1.2510:**  <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1228187>

**LIB:**

**Harpia:**<https://suporte.totvs.com/portal/p/10098/download?e=1050526>

**Onça:**<https://suporte.totvs.com/portal/p/10098/download?e=1168735>

**Menu Reinf** 2.1.2: <https://suporte.totvs.com/portal/p/10098/download?e=1096024>

**Atualização para TAF segregado ou Protheus com Garantia estendida.**

12.1.33: [https://suporte.totvs.com/portal/p/10098/download#detail/1044899](https://suporte.totvs.com/portal/p/10098/download#detail/1043538)  
12.1.2210: [https://suporte.totvs.com/portal/p/10098/download#detail/1084565](https://suporte.totvs.com/portal/p/10098/download#detail/1084563)

***3 - Atualização TSS:***

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)

[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS?source=search)

**Documentação adicional:**

Configuração e aplicação de pacote via VSCode:

[Cross Segmentos - Backoffice Protheus - TAF - Automação fiscal - Como aplicar a atualização do TAF utilizando o Visual Studio Code?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406757164311-Cross-Segmentos-Backoffice-Protheus-TAF-Automa%C3%A7%C3%A3o-fiscal-Como-aplicar-a-atualiza%C3%A7%C3%A3o-do-TAF-utilizando-o-Visual-Studio-Code-?source=search)

Executando o UPDDISTR/UPDTAF:   
<https://www.youtube.com/watch?v=Ya5_foyegTs>

Documentação REINF:

<https://tdn.totvs.com/display/TAF/EFD-Reinf>

<https://tdn.totvs.com/pages/releaseview.action?pageId=587835160#issues-15> <https://tdn.totvs.com/display/public/PROT/EFD-REINF>

**Caso surja alguma dúvida no processo, abrir um chamado com a Equipe do Suporte TOTVS.**
