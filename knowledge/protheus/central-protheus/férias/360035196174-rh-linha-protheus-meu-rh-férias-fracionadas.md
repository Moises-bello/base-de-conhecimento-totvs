---
article_id: 360035196174
category: FÉRIAS
content_hash: 25dc0a4e4b33b79135c14d19a0e8db738d2df645a2a4b2db34ce1be053687a84
fetched_at: '2026-06-28T22:44:34.606093+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH - Férias fracionadas
type: support-article
updated_at: '2026-02-06T20:07:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035196174-RH-Linha-Protheus-MEU-RH-F%C3%A9rias-fracionadas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19229839385239) Tempo aproximado para leitura: 00:03:00 min**  
  
**Dúvida**  
É  possível deixar parametrizado no aplicativo, para que ao solicitar férias, apareça para o funcionário as opções de fracionamento?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Por padrão não há uma forma de apresentar automaticamente ao funcionário quais as opções de fracionamento das férias.   
  
Em caso de fracionamento, **o funcionário poderá solicitar até 3 períodos de férias**, conforme exposto na Reforma Trabalhista, **desde que um dos períodos seja maior ou igual a 14 dias**, e **nenhum dos 3 períodos menor que 5 dias de gozo.**  
  
Para ter essa opção, acessar o **Configurador do Protheus - SIGACFG, e em Ambiente > Cadastros > Parâmetros**, localize o **MV\_REFTRAB,** este parâmetro precisa estar com o conteúdo a seguir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19229823727127)  
  
O conteúdo do parâmetro **MV\_REFTRAB** poderá conter o valor**FSRI**, onde **F**= Férias, **S**= Contribuição Sindical, **R**= Regime Parcial e **I** = Insalubridade Gestante.  
  
Se, por exemplo, o conteúdo do parâmetro **MV\_REFTRAB** esteja **FSI**, os cálculos referentes ao regime parcial serão executados sem as novas orientações da Reforma Trabalhista.  
  
No que tange sobre a ordem cronológica do fracionamento de férias no aplicativo **Meu RH**, submetemos a análise técnica fundamentada no ordenamento jurídico vigente pela RT 13.467/17.  
   
Conforme estabelece o **§1º do Artigo 134 da CLT**, introduzido pela Lei nº 13.467/2017, o gozo das férias pode ser fracionado em até três períodos, desde que haja concordância entre empregado e empregador. Os requisitos cumulativos para tal fracionamento são:  
- Um período não poderá ser inferior a **14 dias corridos**;  
- Os demais períodos não poderão ser inferiores a **5 dias corridos** cada.  
  
**Portanto, inexiste qualquer impedimento legal ou cláusula acessória que obrigue o colaborador a solicitar o período de 14 dias como sendo, obrigatoriamente, a primeira parcela do fracionamento.**  
   
Em observância ao princípio da legalidade, o aplicativo **Meu RH** não impõe o bloqueio de solicitações inferiores a 14 dias para o primeiro período, **visto que tal restrição carece de base legal**.   
  
Desde que o cronograma total de programação de férias do colaborador preveja, em algum de seus três possíveis períodos, a parcela mínima de 14 dias, a operação encontra-se**em plena conformidade com a Reforma Trabalhista.**  
   
**Nota Técnica:** A validação do sistema ocorre sobre o saldo total e o cumprimento das regras de 14 e 5 dias dentro do período concessivo, permitindo a flexibilidade de escala conforme a conveniência entre as partes.  
  
**Saiba Mais**  
[RH - Linha Protheus - MEU RH - Como registrar a solicitação de Férias através do MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058418633)  
[RH - Linha Protheus - MEU RH - É possível solicitar férias em data futura antes de ter completado o período aquisitivo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007705742-RH-Linha-Protheus-MEU-RH-%C3%89-poss%C3%ADvel-solicitar-f%C3%A9rias-em-data-futura-antes-de-ter-completado-o-per%C3%ADodo-aquisitivo?source=search)  
[RH - Linha Protheus - MEU RH - O gestor pode solicitar as férias do funcionário pelo MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402719334551-RH-Linha-Protheus-MEU-RH-O-gestor-pode-solicitar-as-f%C3%A9rias-do-funcion%C3%A1rio-pelo-MEU-RH?source=search)  
[Artigos Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)
