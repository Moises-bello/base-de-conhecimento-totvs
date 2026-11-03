---
article_id: 6846770140823
category: esocial - Periódicos
content_hash: 61e04775b19b7d30deb2f701a01901716b82574b608f8e0a61e98bb36c009478
fetched_at: '2026-06-28T22:47:09.349611+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Erro código 846 - O somatório de cada um dos descontos
  de Contribuição Previdenciária (codIncCP = [31, 32, 34, 35]) e de IRRF (codIncIRRF
  = [31, 32, 33, 34]) não pode ser negativo
type: support-article
updated_at: '2025-02-27T19:55:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6846770140823-RH-RM-FOP-eSocial-Erro-c%C3%B3digo-846-O-somat%C3%B3rio-de-cada-um-dos-descontos-de-Contribui%C3%A7%C3%A3o-Previdenci%C3%A1ria-codIncCP-31-32-34-35-e-de-IRRF-codIncIRRF-31-32-33-34-n%C3%A3o-pode-ser-negativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21162828603927)**Tempo aproximado para leitura: **00:04:30 min****Ocorrência**Ao transmitir folha de pagamento ou rescisão para o governo é retornado a inconsistência **Código de Ocorrência: 846 - Descrição: O somatório de cada um dos descontos de Contribuição Previdenciária (codIncCP = [31, 32, 34, 35]) e de IRRF (codIncIRRF = [31, 32, 33, 34]) não pode ser negativo, ou seja, os vencimentos não podem ser superiores aos descontos.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6846307587351)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Conforme mensagem, a inconsistência é apresentada quando o somatório dos descontos e bases dedutoras (tipos de rubrica 2 e 4) cujo código de incidência de INSS ou IRRF (mensal ou 13º) é menor que o somatório dos proventos e bases (tipo rubrica 1 e 3).    
  
**Solução**  
Acesse o XML do funcionário (RM e TAF) e verifique se, para cada verba relacionada, o tipo de rubrica presente no cadastro da verba do governo corresponde ao tipo da verba no RM (provento no RM como vencimento no Governo; desconto no RM como desconto no Governo; etc.). Se necessário, ajuste o tipo da verba no produto, reencaminhando o S-1010.

Caso os tipos da rubrica estejam corretos, verifique se existe no **ideDmDev** uma verba de restituição de INSS ou IRRF (provento) com valor maior que o de desconto ou sem que exista um valor de desconto no mesmo **ideDmDev**. Conforme regra abaixo, a validação do governo é realizada por demonstrativo de pagamento (**ideDmDev**) presente dentro do XML e não por período de apuração.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6846421433879)

Para os casos de restituição de 13º, o governo apresentou no Perguntas e Respostas a seguinte proposta de solução:   
[- Restituição de INSS de 13º Salário](Gerar%20retifica%C3%A7%C3%A3o%20de%2013%C2%BA%20quando%20existir%20restitui%C3%A7%C3%A3o%20de%20IRRF%20e/ou%20INSS%20na%20rescis%C3%A3o)  
  
Para os casos de **restituição de folha/férias**, não foi apresentada nenhuma proposta pelo governo, sendo então necessário validar diretamente com o governo, visto que a regra utilizada não aceita a verba de provento maior que desconto se não estiverem no mesmo período.   
- [Contato com o governo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432-RH-RM-FOP-eSocial-Contato-com-o-Governo-para-d%C3%BAvidas-sobre-os-eventos-do-eSocial)

**Importante****Em Configurações | Parametrizador | eSocial | Configurações Gerais 6/7**,  foi criado o campo para a informação de um novo evento, **Evento INSS Férias Envelope**, esse evento tem que constar no governo como **desconto****e com incidência em INSS 31 (está incidência é interna do sistema, não havendo necessidade de marcação de flag no evento criado no rm)**. Caso o evento não conste cadastrado corretamente, será necessário realizar o ajuste, enviar o S-1010 de alteração ao governo, com data igual ou anterior ao XML de remuneração que está sendo enviado. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21199459207959)
