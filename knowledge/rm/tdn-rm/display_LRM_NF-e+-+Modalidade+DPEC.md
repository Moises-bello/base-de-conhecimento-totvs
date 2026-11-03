---
content_hash: 2f68ac06a5cee40e8b032d283ca524b98e90bc96ec6a2536af51ce2fc4d6953d
fetched_at: '2026-06-29T00:11:11.417652+00:00'
page_id: '64652349'
product: rm
source: tdn-rm
title: NF-e - Modalidade DPEC
type: documentation
url: https://tdn.totvs.com/display/LRM/NF-e+-+Modalidade+DPEC
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.40* |
| **Processo** | **:** | Modalidade DPEC |
| **Subprocesso** | **:** | Modalidade DPEC |
| **Data da publicação** | **:** | 03/07/2013 |

**Introdução:**

Este tipo de contingência é utilizado quando existe conexão com a internet, porem existe algum problema com o WebService da sefaz (sefaz intermitente ou fora do ar). Ao alterar a modalidade de envio para DPEC a nota será enviada para um WebService diferente, fazendo com que a NF-e tenha dois status (status NF-e e status DPEC). Ao enviar a NF-e em modalidade DPEC a sefaz não realiza consistência dos dados, fazendo com que todas as NF-es emitidas em DPEC sejam autorizadas, possibilitando assim a impressão do DANFE.

**IMPORTANTE:** Para utilizar a modalidade DPEC a NF-e tem que estar com status de “INCONSISTENTE” ou “REJEITADA”. Em hipótese alguma deverá ser enviado em modalidade DPEC a NF-e com status “PENDENTE”. Caso a NF-e esteja “PENDENTE” será necessário criar um novo movimento e transmiti-lo a SEFAZ, onde após normalização da SEFAZ a NF-e que estava como pendente deverá ser cancelada.

**Alterar a modalidade:** Na tela de Nota fiscal eletrônica (Utilitários | Sped | NF-e estadual) vá em: Processos | Alterar modalidade de operação | preencher os dados da filial | alterar a modalidade para DPEC | Preencher o motivo com no mínimo 15 caracteres para que o botão executar seja habilitado | Clique em executar.

**Enviar a NF-e:** Após a alteração da modalidade realize o processo de envio de NF-e normalmente (Processos | Enviar NF-e | preencher o filtro | executar). Ao enviar a NF-e note que a mesma possui dois status (Status NF-e e Status DPEC).

**OBS:** Quando a NF-e é emitida em modalidade DPEC o TSS envia a mesma tanto para o WebService de DPEC quanto para o WebService normal. Devido a isso quando a SEFAZ normalizar basta alterar a modalidade para Normal e realizar a consulta da NF-e novamente.

**Questionamento realizado a SEFAZ:**

**Por que não devo enviar em modalidade DPEC uma NF-e com status de pendente ?**

NF-e foi enviada para a SEFAZ em modalidade normal, mas a SEFAZ saiu do ar antes que a consulta da autorização fosse realizada. Como precisava transportar a mercadoria (pois eram produtos perecíveis) esta mesma nota foi gerada e autorizada em modalidade DPEC normalmente, assim surgiram os seguintes problemas:

1 - Esta NF-e já esta autorizada no primeiro momento (modalidade normal), porque ainda sim o DPEC autorizou? Ele não deveria ter informado que nota já estava autorizada?

2 - Como a nota já estava autorizada a chave gerada pelo DPEC não pode ser autorizada, pois este numero de NF-e já esta autorizado na chave da modalidade normal. Como proceder neste caso visto que o caminhão foi liberado com a DANFE de DPEC?

3 - Posso cancelar o DPEC?

**Resposta da SEFAZ:**

O erro apontado pode estar ocorrendo porque quando é emitida a nota em contingência, não está sendo alterada a numeração da nota. Vamos considerar:

* + O estabelecimento tenta emitir, por exemplo, a NF-e número 10, série 1, na forma “Normal” e por algum motivo não recebe o retorno da SEF/MG;
  + Optando, então, pela emissão em contingência FS-DA, suponhamos que o estabelecimento utiliza a mesma numeração (Nº 10, Série 1), altera a forma de emissão para “Contingência FS-DA”, imprime o DANFE em Formulário de Segurança e circula com a mercadoria;
  + Quando forem sanados os problemas que impediam a transmissão “Normal”, o sistema irá enviar os retornos para todas as notas pendentes, inclusive aquela primeira que foi enviada normalmente antes de detectar os problemas.
  + Por não ter mais essa primeira nota cadastrada no sistema (foi substituída pela de emissão FS-DA), o aplicativo do contribuinte não irá receber esse retorno;
  + Uma vez que os problemas foram sanados, o estabelecimento tenta enviar a nota emitida em FS-DA para obter autorização, mas por divergências no arquivo XML e chave de acesso que já tinha sido autorizada (mesmo sem que o contribuinte tenha recebido o retorno), o sistema rejeita a nota acusando essas inconsistências.

Diante do exposto, reforçamos que **sempre que for enviada uma nota em qualquer uma das contingências**, deverá ser gerada uma **nova NF-e com uma nova numeração**, e assim quando transmitir as NF-e emitidas em contingência receberá o retorno correto.

Após estes procedimentos, será possível tratar as NF-e transmitidas por ocasião da ocorrência dos problemas técnicos que estão pendentes de retorno (estas não terão sido excluídas do aplicativo e terão retorno) cancelando as autorizadas ou inutilizando a numeração das rejeitadas.

Ressaltamos que não poderá haver qualquer alteração da NF-e gerada em contingência nem da sua chave de acesso. A NF-e transmitida deve reproduzir fielmente o DANFE em contingência que acompanhou a circulação da mercadoria (para maiores esclarecimentos, verificar as Orientações de Contingência, constantes a partir da pág. 110 do Manual de Orientação do Contribuinte, acessado através da rota [www.nfe.fazenda.gov.br](http://www.nfe.fazenda.gov.br/) > Documentos > Manuais).

Para regularizar essa situação, o contribuinte que emitiu o documento não autorizado deve prestar uma “Denúncia Espontânea” comprovando que a operação ocorreu de fato e que a mesma foi escriturada no período em que ocorreu.

1. 1. **1.** **Emitir uma nova NF-e, idêntica a ‘NF-e emitida em Contingência DPEC não autorizada e escriturada’, que irá regularizar a escrituração.**

**1.1.** Para essa emissão, o contribuinte poderá utilizar o aplicativo disponibilizado pelo Fisco, no Portal nacional da NF-e: “Emissor de NF-e” ([www.NF-e.fazenda.gov.br/portal/emissor.aspx](http://www.nfe.fazenda.gov.br/portal/emissor.aspx) ) para registrar a NF-e na Base de dados da SEF.

Todos os dados informados na NF-e emitida em Contingência DPEC não autorizada devem ser repetidos, com as seguintes exceções:

• Número da NF-e – informar o número sequencial da NF-e, ou seja, o próximo número a ser utilizado na data de emissão da nova NF-e;

• Data de emissão – informar a data da nova NF-e emitida para regularizar a situação;

• Data de saída – não informar;

• Finalidade de emissão da NF-e = 3 – NF-e de ajuste / Processo de emissão da NF-e = 3 - emissão NF-e pelo contribuinte com aplicativo fornecido pelo Fisco (caso seja adotada a sugestão acima);

• Informações Complementares = Além das existentes, acrescentar:

“Para efeitos de escrituração considera-se como data de emissão desta NF-e: -  dd/mm/aaaa, que foi a data em que a operação ocorreu de fato. Substitui NF-e emitida nesta data com tipo de emissão “Contingência DPEC”, número do Protocolo de autorização da DPEC nº xxxxxxxxxxxxx.

Regularização conforme Denuncia Espontânea, Protocolo nº ........, na AF .............”

**1.2.** Após confirmar a autorização da NF-e, acertar a escrituração fiscal.

Se essa operação já foi escriturada em período anterior, essa nova NF-e deverá ser escriturada sem débito do imposto apenas referenciando o documento escriturado anteriormente e a denúncia espontânea.

Se o contribuinte for obrigado à EFD, ele deve fazer o acerto no período em que a NF-e não autorizada foi escriturada:

• Lançar “Observação de lançamento fiscal” no documento (Reg. C195):

“NF-e emitida em Contingência DPEC, protocolo autorização DPEC Nº xxxxx e não autorizada. Regularizada em  dd/mm/aaaa, por Denuncia Espontânea, Protocolo nº ........, na AF .............”;

• Alterar o número da Chave de acesso informada no reg. C100;

• Substituir a EFD.

1. 1. **2.** **Informar ao contribuinte destinatário as seguintes informações para que ele proceda aos acertos necessários para regularizar a escrituração desta NF-e nos termos da Denúncia Espontânea, além de enviar, para o mesmo, o xml da NF-e devidamente autorizada:**

**2.1.** Se a ‘NF-e emitida em Contingência DPEC’ não tiver sido escriturada no período em que a mercadoria foi recebida:

• Fazer o lançamento de documento extemporâneo, considerando o XML da NF-e devidamente autorizada;

• Lançar ‘Observação de lançamento fiscal’ no documento:

“NF-e emitida por DPEC – protocolo n.º ........... e não transmitida, regularizada em  dd/mm/aaaa, por Denuncia Espontânea, Protocolo nº ........, na AF .............”.

**2.2.** Se a NF-e não autorizada tiver sido escriturada no período em que a mercadoria foi recebida e o contribuinte for obrigado à EFD, fazer o acerto no período em que a NF-e não autorizada foi escriturada:

• Lançar ‘Observação de lançamento fiscal’ no documento:

“NF-e emitida e não autorizada regularizada em  dd/mm/aaaa, por Denuncia Espontânea, Protocolo nº ........, na AF .............”;

• Alterar o número da Chave de acesso informada no reg. C100;

• Substituir a EFD.

Importante frisar que o crédito do ICMS só poderia ter sido utilizado após a autorização da NF-e. Portanto, caso o contribuinte tenha utilizado o crédito, isso deve ficar claro na denúncia espontânea e deve estar devidamente comprovada a escrituração do débito pelo emitente da NF-e à época própria.

**2.2.1.** Se não houve o lançamento do crédito no período em que a NF-e foi escriturada:

• Fazer o lançamento do crédito como “outros créditos”, no período atual.

Na EFD, gerar reg. E111, utilizando código de “Ajuste de apuração” = “MG029999” e o campo descrição complementar do ajuste = “Documento de entrada lançado sem o crédito em período anterior”. Gerar o reg. E113 identificando o documento que foi lançado sem o crédito.

O link para acessar os endereços e dados das AF é <http://www.fazenda.mg.gov.br/secretaria/enderecos/admfazendaria.html> .

“Qualquer outra informação ou esclarecimento sobre dispositivos da legislação tributária, que não se revista das características e dos requisitos próprios de consulta (RPTA/MG, artigo 37, aprovada pelo Decreto nº. 44.747 de 03 de março de 2008), será prestado verbalmente ao interessado pela Administração Fazendária do município de circunscrição do contribuinte, conforme disposto no art. 48 do diploma legal citado”.

*\*As dúvidas esclarecidas por esta mensagem têm caráter de orientação não gerando o efeito decorrente da consulta formal.*

Atenciosamente,

**Central de Atendimento da SEF/MG**

Diretoria de Gestão de Atendimento ao Público (DGAP)

Superintendência de Arrecadação e Informações Fiscais (SAIF)

Secretaria de Estado de Fazenda (SEF/MG)

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
