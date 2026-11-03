---
article_id: 36814407779991
category: Meu RH - Pagamento
content_hash: 50b45fff6ce651113c50ed767fd21b0b93be0ae21781dbbe7af43bc78c20774b
fetched_at: '2026-06-28T22:47:33.846085+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: RH - RM - Meu RH - Como Gerar o Demonstrativo de Pagamento com relatório via
  SmartView
type: support-article
updated_at: '2026-01-08T13:01:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36814407779991-RH-RM-Meu-RH-Como-Gerar-o-Demonstrativo-de-Pagamento-com-relat%C3%B3rio-via-SmartView
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36814407754391) Tempo aproximado para leitura: **00:01:05min**  
  
**Dúvida**  
Como Gerar o Demonstrativo de Pagamento com relatório via SmartView?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.2302  
  
**Solução**  
Para utilizar o relatório demonstrativo de pagamento via SmartView no Meu RH, é fundamental realizar a importação do relatório **FOPTRP0013**. Essa importação deve ser feita por meio do menu **Gestão | Totvs Compartilhamento**. Você pode consultar o passo a passo detalhado para este processo clicando [AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7781155867543-RH-RM-FOP-Importa%C3%A7%C3%A3o-de-relat%C3%B3rios-e-layouts-atrav%C3%A9s-do-Totvs-Compartilhamento).

O próximo passo é cadastrar a categoria do relatório. Isso deve ser feito acessando o menu **Gestão | SmartView | Categorias**. Durante esse cadastro, é necessário vincular a categoria os perfis dos usuários do Meu RH e um perfil de usuário que seja administrador, mestre ou que possua permissão total no módulo de **Folha de Pagamento**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36814413010071)

Com a categoria criada, o próximo procedimento é associá-la ao relatório **FOPTRP0013**. Essa associação deve ser realizada na tela inicial do SmartView, permitindo que o relatório esteja corretamente categorizado e acessível conforme as permissões definidas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36814413013271)

Em seguida, é necessário associar o relatório ao grupo de quiosque dos funcionários. Essa associação deve ser feita através do menu **Configurações | Parametrizador | RM Portal**. Esse passo é fundamental para que os funcionários possam realizar o dowload do relatório no Meu RH e garantindo a disponibilidade do demonstrativo de pagamento para consulta.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36814628210839)

Após a conclusão do processo de parametrização, o relatório estará disponível para download no Meu RH.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36817146667031)

Para obter mais informações detalhadas sobre a configuração do SmartView e sua integração com o RM, consulte o link: [Configuração do Smart View para integrar ao RM](https://tdn.totvs.com/pages/releaseview.action?pageId=706142061).
