---
article_id: 17085108412567
category: eSocial - Gerar XML/ Integração Evento
content_hash: 9eb83bb0990de5ad72842aaf3a41a16f4cd6c803c0a50197d78538340742e5f3
fetched_at: '2026-06-28T22:47:11.915718+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao gerar o evento S-1200 ocorre erro: O campo ''tpInsc''
  do registro ''sucessaoVinc'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2026-03-17T22:06:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17085108412567-RH-RM-FOP-eSocial-Ao-gerar-o-evento-S-1200-ocorre-erro-O-campo-tpInsc-do-registro-sucessaoVinc-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17085102096407) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao gerar o XML S-1200 ocorre o erro: O campo 'tpInsc' do registro 'sucessaoVinc' é obrigatório e não está preenchido. Este erro é seguido de outros três erros: O valor informado no campo CPF/CNPJ Empregador Anterior não é válido; O campo 'nrInsc' do registro 'sucessaoVinc' é obrigatório e não está preenchido; O campo 'matricAnt' do registro 'sucessaoVinc' é obrigatório e não está preenchido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17084154332823)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**  
O erro ocorre no momento de gerar o XML S-1200 que foi transferido entre coligadas ou, ao gerar o XML S-1200 de rescisão complementar, sendo que em qualquer um dos casos não foram preenchidas as informações de sucessão de vínculo.  
  
**Solução**  
Para correção da ocorrência favor realizar as validações abaixo:  
• **Transferência entre coligadas**  
1. Identifique o funcionário transferido na nova coligada (funcionário com o cadastro ativo) e preencha as informações na aba **Sucessão de Vínculo**.

![](https://totvssuporte.zendesk.com/attachments/token/gqknsQEJmEXzionEsGpFYhEiS/?name=image.png)

2. Após gere o XML novamente.

• **Rescisão Complementar**  
1. Identifique o acordo vinculado à rescisão complementar e verifique se a opção **Pagamento de verbas devidas pela empresa sucessora a empregados desligados ainda na sucedida**consta marcado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17084132528663)

2. Verifique se a informação condiz com a situação do empregado.

2.1. Caso não esteja condizente com a situação do empregado, desmarque a opção;

2.2. Caso esteja condizente com a situação do empregado, será necessário preencher o cadastro do funcionário demitido com o tipo de admissão "T-Ent Transf sem ônus p/ Cedente" e os dados da sucessão de vínculo cadastrado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17084704062487)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17084748725015)

3. Após alterações, gere novamente o XML.  
  
**Saiba Mais**  
Para saber mais consulte o link abaixo:  
- [Como realizar a geração do evento S-1200 com a tag remunSuc com valor "S"?](https://tdn.totvs.com/pages/releaseview.action?pageId=461910281)   
- [- Transferência entre filiais ou coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020186252-RH-RM-FOP-Transfer%C3%AAncia-entre-filiais-ou-coligadas)
