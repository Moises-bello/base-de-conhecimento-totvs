---
article_id: 39077991168791
category: RH - Definições de Cálculo
content_hash: 53354222a24345a0fa4f9a3ae0c300a2bfe387e2100c114327fe2f243e8cb6e0
fetched_at: '2026-06-28T22:43:22.433290+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Compartilhamento SRY, SRM e RGA
type: support-article
updated_at: '2026-03-16T18:40:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39077991168791-RH-Linha-Protheus-GPE-Compartilhamento-SRY-SRM-e-RGA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39077991158807) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao acessar a rotina de Cadastro de Roteiros o sistema gera a mensagem:  
Help: O compartilhamento das tabelas SRY, SRM e RGA deve ser idêntico. Verifique a Configuração   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2310  
  
**Causa**  
Compartilhamento das tabelas SRY, SRM e RGA diferentes.   
  
**Solução**  
A **tabela RGA é dependente (filha) da SRY** e, portanto, **não pode possuir compartilhamento diferente** da tabela pai. Caso isso ocorra, haverá perda de registros e quebra do vínculo entre as tabelas.

Ao acessar a rotina de Cadastro de Roteiros, o sistema busca os dados na RGA com base no roteiro posicionado e na filial da SRY. Com o compartilhamento divergente entre as tabelas, não é possível localizar os registros correspondentes, inviabilizando o funcionamento correto da rotina.

**Exemplo de compartilhamento correto:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/39078020736023)**

**Atenção:** A imagem acima é apenas um exemplo de que as tabelas devem possuir compartilhamento iguais. A empresa deve avaliar qual será a configuração das tabelas em seu ambiente.

**Saiba Mais**  
[Documentação técnica](https://tdn.totvs.com/display/PROT/25331576+DRHCALCPRT-18902+DT+Compartilhamento+divergente+entre+a+SRY+e+a+RGA)  
[RH - Linha Protheus - GPE - Como recriar apenas roteiros e fórmulas do módulo 07 - Gestão de Pessoal - SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044572434-RH-Linha-Protheus-GPE-Como-recriar-apenas-roteiros-e-f%C3%B3rmulas-do-m%C3%B3dulo-07-Gest%C3%A3o-de-Pessoal-SIGAGPE)
