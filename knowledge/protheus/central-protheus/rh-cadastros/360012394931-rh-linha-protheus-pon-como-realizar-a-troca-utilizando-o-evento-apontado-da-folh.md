---
article_id: 360012394931
category: RH - Cadastros
content_hash: 5c6a908e5ff1b1e1c78592982abf880a96bacd9da05a8ae2ee2e3a6da6a9bd53
fetched_at: '2026-06-28T22:44:53.137485+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH – Linha Protheus – PON – Como realizar a troca utilizando o evento apontado
  da folha para banco de horas ou vice-versa, mantendo o desconto e demonstrando a
  informação nas observações do Espelho de Ponto?
type: support-article
updated_at: '2025-12-22T13:22:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012394931-RH-Linha-Protheus-PON-Como-realizar-a-troca-utilizando-o-evento-apontado-da-folha-para-banco-de-horas-ou-vice-versa-mantendo-o-desconto-e-demonstrando-a-informa%C3%A7%C3%A3o-nas-observa%C3%A7%C3%B5es-do-Espelho-de-Ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34257896379927) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como realizar a troca utilizando o evento apontado da folha para banco de horas ou vice-versa, mantendo o desconto e demonstrando a informação nas observações do espelho de ponto?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acessar a configuração de parâmetros, via Configurador(SIGACFG):

* Entre no sistema onde a configuração de parâmetros é realizada. Utilize com base a documentação: [Parâmetros do sistema - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=381037132)
* **Ajustar os parâmetros**:
  + Localize os parâmetros `MV_ABOSEVE` e `MV_SUBABAP` na área de configuração de parâmetros e ajuste-os com os conteúdos igual à S;

2. Acesse a rotina de **Motivo de Abono**, utilize a documentação: [RH - Linha Protheus - PON - Como cadastrar Motivos de Abono/Justificativa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000047328-RH-Linha-Protheus-PON-Como-cadastrar-Motivos-de-Abono-Justificativa), cadastre o motivo de abono com as seguintes configurações:  
- Campo **Abona Horas** como **NÃO;**

- Campo **Cód. Evento** informar um evento válido que seja configurado para banco de horas;  
Veja mais detalhes na tela abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744641260055)  
Já no cadastro de evento, em Atualizações > Cadastro do Ponto > Eventos, filtre o evento vinculado ao motivo de abono, no caso o 209. Veja o cadastro do evento para desconto no BH:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744641261463)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744580253079)  
- Já para a troca com evento de banco de horas para folha, veja exemplo:  
Motivo de abono:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744580254871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744580256919)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744641272727)  
3. Para troca de evento no apontamento siga o procedimento:  
Em Atualizações > Lançamentos > Integrados filtre o funcionário e em Outras Ações > Alterar;  
Selecione o dia e clique na linha do apontamento clique no botão ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744580265495) 'Abonar/Justificar-<F7>' e preencha o abono conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744641276055)  
Ao abrir a tela de manutenção de Abonos/Justificativas, faça o lançamento do motivo de abono conforme exemplo abaixo e clique em salvar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744580267927)  
Após lançar o abono clique em salvar que ficará gravado o lançamento de abono para troca de evento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744641278743)

4. Execute o **cálculo mensal,** utilize como base a documentação: [**RH - Linha Protheus - PON - Como fazer e qual a finalidade do Cálculo Mensal**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550453-RH-Linha-Protheus-PON-Como-fazer-e-qual-a-finalidade-do-C%C3%A1lculo-Mensal)

5. Acesse banco de horas e observe que o evento selecionado será apresentado  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744580272791)

6. Veja como ficou em observação no Espelho de Ponto:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28744641281559)  
  
**Importante**  
- O evento que estava informado no motivo de abono foi enviado para banco de horas;  
- No espelho de ponto apresentou a observação do abono;  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Orientações de como incluir uma Observação no Espelho de Ponto, sem utilização de motivo de abono cadastrado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405097147927-RH-Linha-Protheus-PON-Orienta%C3%A7%C3%B5es-de-como-incluir-uma-Observa%C3%A7%C3%A3o-no-Espelho-de-Ponto-sem-utiliza%C3%A7%C3%A3o-de-motivo-de-abono-cadastrado)
