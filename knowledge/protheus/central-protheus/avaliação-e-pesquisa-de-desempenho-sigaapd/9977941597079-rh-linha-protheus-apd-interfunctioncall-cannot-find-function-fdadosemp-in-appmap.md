---
article_id: 9977941597079
category: Avaliação e Pesquisa de Desempenho (SIGAAPD)
content_hash: d8733a8e1c1d36b43946612375ab6e58beca55b833b120909fadd45e9997f747
fetched_at: '2026-06-28T22:42:53.882289+00:00'
product: protheus
section_id: 206956088
source: central-protheus
title: 'RH - Linha Protheus - APD - InterFunctionCall: cannot find function FDADOSEMP
  in AppMap'
type: support-article
updated_at: '2022-11-03T13:11:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9977941597079-RH-Linha-Protheus-APD-InterFunctionCall-cannot-find-function-FDADOSEMP-in-AppMap
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:30 min****Dúvida***InterFunctionCall*: *cannot* *find* *function* FDADOSEMP *in AppMap*  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH – A partir da versão 12.33  
  
**Solução**No módulo 53 - SIGAAPD, quando é criado um participante, o erro ***"InterFunctionCall: cannot find function FDADOSEMP in AppMap",***ou simplesmente, função não encontrada FDADOSEMP, ocorre no Sistema.  
  
Vale ressaltar que, quando temos o estouro de um erro, nesse sentido, em tela, também é gerado um errorlog no **arquivo consolelog na pasta do appserver.** Neste caso em específico, o *errorlog* é o que envio abaixo, no *print*:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9977759440791)  
  
Ao avaliar o *errorlog* apresentado, é possível notar que o sistema está tentando, no momento do erro, **utilizar uma função de nome FDADOSEMP**, que **não existe no repositório**, deste modo, causando o erro de **"função não existe"**.  
  
Entretanto, ao avaliar o momento em que o erro ocorre, é possível avaliar que ele é chamado na execução da propriedade **"Validação Sistema"** do campo **RD0\_FIL**, como pode verificar abaixo, o trecho retirado deste *errorlog:*![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9977831411735)  
**De fato, essa função FDADOSEMP não existe em repositórios mais recentes, possivelmente tendo sido excluída de onde ela era existente, por estar desatualizada ou ter sido substituída.**  
  
Ocorre, que o campo que chama esta função, sendo o RD0\_FIL, da tabela RD0, entretanto, em ambientes mais atualizados e padrões, com todas as atualizações de fontes e dicionários mais recentes, **este campo RD0\_FIL não existe na estrutura da tabela RD0** e, por premissas de implementação, campos desatualizados, substituídos ou obsoletos, continuam sempre a existir na estrutura da tabela, **apenas sendo desativados e não mais preenchidos**, porém, como pode ver abaixo, na estrutura padrão, não existe este campo em questão:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9977843156631)  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9977844320407)  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9977858795799)  
Deste modo, para que haja correção deste erro, é possível seguir **uma das alternativas abaixo**:  
> Desativar/excluir este campo da estrutura da tabela RD0 (e consequentemente ajustar a ordem dos campos seguintes) recriando sua tabela RD0, para que ela assuma a nova estrutura, **sem a presença deste campo RD0\_FIL**;  
> **Excluir o uso da função FDADOSEMP** deste campo (e de possíveis outros que possam tê-lo), ajustando a validaão deste campo, conforme sua necessidade.  
  
Após este ajuste na estrutura da tabela, o erro não deve mais ser apresentado no momento de realizar o Cadastro ou o Relacionamento de Participantes.  
  
Veja mais sobre relacionamento dos participantes:  
[RH - Linha Protheus - MEU RH - Como relacionar os Participantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050255013-RH-Linha-Protheus-MEU-RH-Como-relacionar-os-Participantes?source=search)  
  
Orientamos também que, é necessário efetuar a alteração da configuração do campo abaixo, e deixar como o padrão, conforme *print*:  
  
![](https://totvssuporte.zendesk.com/attachments/token/A6fsDyMgOS5qShLHIcdeRuZvo/?name=image.png)  
  
**Saiba Mais**[Artigos sobre Avaliação Pesquisa e Desempenho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206956088-Avalia%C3%A7%C3%A3o-e-Pesquisa-de-Desempenho-SIGAAPD-)  
[Artigos sobre Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-Portal-de-Gest%C3%A3o-de-Capital-Humano)  
[Artigos sobre Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-Meu-RH)
