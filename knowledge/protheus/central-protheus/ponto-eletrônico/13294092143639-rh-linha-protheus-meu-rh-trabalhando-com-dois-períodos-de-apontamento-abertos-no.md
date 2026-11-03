---
article_id: 13294092143639
category: PONTO ELETRÔNICO
content_hash: 9143ec4412274988b86a28cccaaf38abcb5008efdf7ce6da98516ac205261e94
fetched_at: '2026-06-28T22:44:36.618381+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Trabalhando com dois períodos de apontamento
  abertos no App Meu RH
type: support-article
updated_at: '2025-07-04T18:56:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13294092143639-RH-Linha-Protheus-MEU-RH-Trabalhando-com-dois-per%C3%ADodos-de-apontamento-abertos-no-App-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27269104586519) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Trabalhando com dois períodos de apontamento abertos no App Meu RH  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas as versões   
  
**Solução**Inicialmente, cabe ressaltar que, **tanto no App Meu RH**, ou no módulo **SIGAPON - Ponto Eletrônico**, **não é recomendado** o trabalho com dois, ou mais, períodos de apontamento abertos de forma simultânea.  
   
O que ocorre, no módulo SIGAPON - Ponto Eletrônico, **é a manutenção do Período ainda não encerrado**, ou seja, para que seja possível visualizar as marcações do próximo período e realizar alguns ajustes futuros.   
  
Porém o controle correto do **Período Aberto no Ponto Eletrônico**, é dado pelos parâmetros **MV\_PAPONTA e MV\_PONMES**, ou seja, somente **um período consegue existir nesse parâmetro**, deste modo somente **um período fica aberto por vez.**   
  
Entretanto, é comum não realizar o fechamento do período anterior, no exato dia em que o período se encerra, sendo comum estender esse período por alguns dias, deste modo, **realizando a alteração do conteúdo do parâmetro** (ou do período aberto) manualmente, porém sem fechá-lo.  
   
Em consonância ao exposto acima, no App Meu RH, temos **uma validação para criação do Período Futuro**, assim como documentado no *link* abaixo:  
[RH - Linha Protheus - MEU RH - Como verificar o espelho de ponto em período futuro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5223165502359-RH-Linha-Protheus-MEU-RH-Como-verificar-o-espelho-de-ponto-em-per%C3%ADodo-futuro?source=search)  
   
Com o auxílio do parâmetro **MV\_MRHDPER**, **é somado o valor do parâmetro ao último dia do período atualmente aberto**, para que acessos realizados pelo App Meu RH, a partir dessa data resultante, **sejam demonstrados o período futuro de forma projetada para o usuário.  
  
Exemplo:**Todos os períodos abaixo do *print*, estão já tratados e fechados pelo SIGAPON.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29062905287831)  
  
**A data de hoje, dia da elaboração deste artigo é 08/01/2025**, portanto, temos nesse ambiente, dois períodos de apontamento abertos, que são **01/12/2024 - 31/12/2024 e 01/01/2025 - 31/01/2025.**No botão Modificar Período > Apenas Visualizar, trará o período pelo MV\_PONMES, que está aberto inicialmente:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29062905291671)  
  
Tendo o parâmetro **MV\_MRHDPER com o conteúdo 1**, quer dizer que 1 dia após o término do período aberto (**01/12/2024 a 31/12/2024**), o próximo período (**Janeiro/2025**) já estará no App Meu RH, projetado para inclusões e manutenções.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29062929950743)  
 **Importante frisar que,** tendo dois períodos de apontamento abertos no SIGAPON, o parâmetro MV\_PONMES demonstrado acima, para funcionalidade correta, sempre precisará estar cadastrado no primeiro período aberto.   
  
Ou seja, neste exemplo, se por ventura, o **MV\_PONMES estiver como 01/01/2025 a 31/01/2025,** não haverá essa projeção do próximo período, pois só terá funcionalidade para o período seguinte, nunca para o anterior. **Saiba Mais  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
