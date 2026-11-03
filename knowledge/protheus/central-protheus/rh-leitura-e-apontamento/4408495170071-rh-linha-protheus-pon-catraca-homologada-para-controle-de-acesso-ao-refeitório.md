---
article_id: 4408495170071
category: RH - Leitura e Apontamento
content_hash: 8f4892bd229b2586b74567c3c1025e8c8d076c3077f1a73f08f8244e713ec6f2
fetched_at: '2026-06-28T22:44:46.048670+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON- Catraca homologada para controle de acesso ao refeitório
type: support-article
updated_at: '2025-08-14T19:28:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408495170071-RH-Linha-Protheus-PON-Catraca-homologada-para-controle-de-acesso-ao-refeit%C3%B3rio
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34185778627607) Tempo aproximado para leitura: 00:01:00 min**  
  
Dúvida**Validação de catraca homologada para controle de acesso ao refeitório.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Se a catraca gerar um **arquivo txt** com o registro das refeições, **SIM** ela é homologada pelo Protheus.   
A [**leitura de refeição**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19222215435927-RH-Linha-Protheus-PON-Como-cadastrar-um-rel%C3%B3gio-para-leitura-e-grava%C3%A7%C3%A3o-das-refei%C3%A7%C3%B5es-contidas-no-arquivo-TXT-de-Ponto), é efetuada através do campo Nº crachá do funcionário **(****RA\_CRACHA)** dentro do Cadastro de Funcionários **(Atualizações>Cadastro de Funcionários>Funcionários, aba relógio registrador)**, com algumas particularidades no arquivo a ser gerado **diferentemente da leitura das marcações;**  
  
Para refeitório, **não entramos no modelo AFD com o PIS ou CPF**, então basta que a catraca gere as informações num arquivo txt, da seguinte maneira:  
**-** **Código** = gerar com **6 posições** o código do crachá do funcionário **(não o PIS nem CPF)**, o campo **RA\_CRACHA** deve estar preenchido com este conteúdo;  
**-** **Relógio** = se for utilizar o número do relógio passar o código sempre com **3 posições o código do Relógio**(o mesmo código cadastrado no relógio no Protheus - tabela SP0);  
- **Dia, Mês, Ano, Horas e Minutos** = gerar com as posições, sem as barras, o cadastro de cada informação;  
  
Com esse arquivo txt, cadastrar as posições no relógio seguindo as documentações abaixo:  
[- Como fazer a Leitura/Apontamento de marcações vindas de um relógio que não é REP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007362931-MP-PON-Como-fazer-a-Leitura-Apontamento-de-marca%C3%A7%C3%B5es-vindas-de-um-rel%C3%B3gio-que-n%C3%A3o-%C3%A9-REP)  
[- Cadastro de Refeições no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018129092-MP-PON-Cadastro-de-Refei%C3%A7%C3%B5es-no-Ponto-Eletr%C3%B4nico)  
  
Agora, **para uma integração direta via *XML***, somente com o programa [**Suricato**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16779731236119-RH-Linha-Protheus-PON-x-Suricato-Integra%C3%A7%C3%A3o-Protheus-x-Suricato), da nossa parceira Telemática.   
  
Para maiores informações sobre o Suricato e a obtenção dele, entre em conato com seu **ESN - Gerente de Contas TOTVS** para apresentações e propostas comerciais.  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
