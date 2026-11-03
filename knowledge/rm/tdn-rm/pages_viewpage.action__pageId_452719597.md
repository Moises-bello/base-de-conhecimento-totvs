---
content_hash: 2b34eadce28744f2c74a7ca43f2a1a0ff7ba4a22785523178c80565c5cdc7f4a
fetched_at: '2026-06-29T00:10:08.857904+00:00'
page_id: '452719597'
product: rm
source: tdn-rm
title: Configurações Gerais 5/7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719597
version: 14
---

Nesta aba é possível fazer as Configurações Gerais relacionadas ao eSocial:   
   
**Gestão de Pessoas (Vitae) / Segurança e Saúde Ocupacional (SMT)**    
  
   
**Considerar registros do Vitae**  
Marcando este flag serão levadas na geração do XML S2200(TAG observação) as informações do curso/turma que possui o flag "curso eSocial" marcado.   
    
**Considerar avaliações das turmas de treinamento do Vitae**  
Serão levados somente as informações do curso/turma que possui o flag "curso eSocial" marcado e que possui avaliação de conhecimento ou qualidade para o funcionário.  
    
**Considerar evento Toxicológico do SMT**   
Quando este parâmetro estiver *marcado* o sistema irá considerar os exames cadastrados no SMT na geração de XML S2200 e S2299 na TAG observação.   
Quando *desmarcado* ao gerar o XML a tag observação será preenchida com as informações contidas no anexo/Folha de Pagamento /Observações Contratuais.  
   
   
**Retificação folha/rescisão**  
Período inicial deve ter o valor entre 10000 e 30000 e será gravado no mês competência do fato gerador da rescisão ou folha de pagamento, ou seja, será inserido novo período no mesmo mês em que a rescisão ou folha de pagamento foi calculada.

**Unificar período na retificação**

Quando ativado, o sistema passa a unificar a geração dos XMLs de retificação, o que significa que os eventos registrados nos períodos de retificação são agora consolidados no período original.

Importante!

1. Inicialmente, este parâmetro não unificará as retificações de rescisão.
2. É essencial executar o atualizador para garantir o correto funcionamento do processo de unificação, pois, a partir das versões mais recentes, os eventos com o mesmo código terão seus valores somados.

**Não Lançar Liquido de Retificação no Envelope da Competência Atual**

Quando este parâmetro estiver marcado o sistema passa a lançar os valores com a data de pagamento atual no período da retificação, dessa forma não é informado nenhum valor no período atual.

**Considerar Prefixo Período Funcionário apenas a partir da competência**   
Informe a data que será considerado o parâmetro no cadastro de funcionários referente a "Prefixo Período (eSocial)" para informação na geração de XML. Esta data servirá para controle de quando a informação da tag <ideDmDev> deve ter ou não o prefixo considerado por exemplo nos eventos S-1200, S-1210, S-2299, S-2399.

**Observação:**  
Competência a partir da qual será considerado o prefixo do período não pode ser anterior a data de início dos eventos periódicos.

|  |  |
| --- | --- |
|  | Informações Complementares |

eSocial

[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)
