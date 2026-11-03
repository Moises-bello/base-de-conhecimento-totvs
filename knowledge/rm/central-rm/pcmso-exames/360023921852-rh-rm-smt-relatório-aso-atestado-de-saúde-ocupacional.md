---
article_id: 360023921852
category: PCMSO / Exames
content_hash: d0b46c5d10aea970db7236d33b2369210fc74ab042bdc254f175be414074fc86
fetched_at: '2026-06-28T22:47:42.179636+00:00'
product: rm
section_id: 1500000861462
source: central-rm
title: RH - RM - SMT - Relatório ASO - Atestado de Saúde Ocupacional
type: support-article
updated_at: '2026-06-01T12:15:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023921852-RH-RM-SMT-Relat%C3%B3rio-ASO-Atestado-de-Sa%C3%BAde-Ocupacional
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16039709976599) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Como gerar relatório ASO?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - Todas as Versões  
  
**Solução**

Para gerar o relatório do ASO, basta clicar na opção **Imprimir ASO**, localizada no **Prontuário Médico** o mesmo carregará as informações do exame exibido na visão e o relatório será gerado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26793029360023)

O relatório padrão é disponibilizado com base nas informações da NR-7:  
Item 7.5.19.1 e o ASO deve conter no mínimo:

*a) razão social e CNPJ ou CAEPF da organização;*

*b) nome completo do empregado, o número de seu CPF e sua função;*

*c) a descrição dos perigos ou fatores de risco identificados e classificados no PGR que necessitem de controle médico previsto no PCMSO, ou a sua inexistência;*

*d) indicação e data de realização dos exames ocupacionais clínicos e complementares a que foi submetido o empregado; e) definição de apto ou inapto para a função do empregado;*

*f) o nome e número de registro profissional do médico responsável pelo PCMSO, se houver;*

*g) data, número de registro profissional e assinatura do médico que realizou o exame clínico.*

O relatório ASO é um relatório interno do sistema. Está atrelado ao código fonte, e portanto, não há estrutura disponível para modificação no RM Reports, como no relatorio espelho do cartão de ponto, por exemplo.

Caso a empresa deseje ter uma relatório personalizado, deverá ser desenvolvido um relatório pela própria empresa com base nos ajustes desejados, que será gerado pela rotina **Gestão** | **RM Reports**.   
  
**Saiba mais**

Para maiores informações, acesse:

[- TDN - Atestado de Saúde Ocupacional](http://tdn.totvs.com/pages/viewpage.action?pageId=452719163)   
[- Erro relatorio ASO: dados de identidade do paciente e o registro do médico que realizou a consulta](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009555671-TOTVS-RH-Linha-RM-SMT-Erro-relatorio-ASO-dados-de-identidade-do-paciente-e-o-registro-do-m%C3%A9dico-que-realizou-a-consulta)  
[- Erro ao gerar relatorio ASO: Responsável pela Monitoração Biológica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011007231-TOTVS-RH-Linha-RM-SMT-Erro-ao-gerar-relatorio-ASO-Respons%C3%A1vel-pela-Monitora%C3%A7%C3%A3o-Biol%C3%B3gica#:~:text=Documenta%C3%A7%C3%B5es-,TOTVS%20RH%20-%20Linha%20RM%20-%20SMT%20-%20Erro%20ao%20gerar%20relatorio,ASO%3A%20Respons%C3%A1vel%20pela%20Monitora%C3%A7%C3%A3o%20Biol%C3%B3gica&text=Ao%20gerar%20o%20relat%C3%B3rio%20ASO,a)%20do%20Programa%20de%20PCMSO.)
