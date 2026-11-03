---
article_id: 17887407781271
category: esocial - Processos
content_hash: a99f2e4d99840fc32180cf924ac3b150bc43a10a5724c0d02c78fc339dd8ff82
fetched_at: '2026-06-28T22:47:08.377323+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: 'RH - RM - FOP - eSocial - FGTS Digital: Remuneração para fins rescisórios'
type: support-article
updated_at: '2026-04-17T18:06:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17887407781271-RH-RM-FOP-eSocial-FGTS-Digital-Remunera%C3%A7%C3%A3o-para-fins-rescis%C3%B3rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17887366300695) Tempo aproximado para leitura: **00:03:40 min**  
  
**Dúvida**  
Como o sistema TOTVS - Linha RM se comporta em relação à remuneração para fins rescisórios no FGTS Digital?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir das Versões 12.1.2310.180, 12.1.2402.115 e Superiores.  
  
**Solução**

Elaboramos um guia para auxiliá-lo no preenchimento do campo referente aovalor da **Remuneração para Fins Rescisórios**, utilizamos como referência o [Manual do FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica), disponível na página oficial do governo.

Lembrando que, este preenchimento é necessário somente em caso de desligamento que abrange período trabalhado anterior à obrigatoriedade do eSocial ou quando não houver informação das remunerações registrada no sistema do FGTS Digital.  
  
**É importante destacar que o próprio sistema FGTS Digital emitirá um alerta quando forem identificadas a falta de remuneração do funcionário durante o período em que o funcionário trabalhou na empresa.**  
  
O empregador tem duas maneiras de adicionar os valores faltantes:

* **Método 1: Informação das remunerações faltantes**

Desde a entrada do eSocial, as informações sobre verbas foram enviadas ao ambiente do Governo através do evento S-1200. Estes valores irão compor a Remuneração para Fins Rescisórios. Contudo, caso ocorram problemas na integração desses valores ou o funcionário tenha sido admitido antes do eSocial, é necessário informar o saldo remanescente.

Através do MÉTODO 1, o usuário tem a possibilidade de inserir todas as remunerações faltantes, seja diretamente na tela do programa ou importando os valores através de um arquivo TXT.

**1.1 Inclusão dos dados na tela do sistema**  
Na primeira opção, o empregador poderá incluir os valores faltantes diretamente na tela de Gestão de Histórico de Remunerações do sistema FGTS Digital, editando os campos disponíveis.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22149709916951)

**1.2 Importação do Histórico de Remunerações**  
Nesta opção, é necessário gerar um arquivo TXT e importá-lo para o sistema FGTS Digital. Será possível criar o arquivo seguindo as orientações do [Leiaute FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/fgts-digital-leiaute-arquivo-recomposicao-historico-do-vinculo) utilizando a ferramenta de relatório disponível no TOTVS Folha de Pagamento, ou através do [**Arquivo FGTS Digital**](https://tdn.totvs.com/pages/releaseview.action?pageId=830963089#FGTSDigitalArquivoSimplificadopararecomposi%C3%A7%C3%A3odohist%C3%B3ricodov%C3%ADnculodotrabalhador-4) que a TOTVS disponibilizou para exportação. 

**Atenção!** Recomendamos o uso do arquivo de importação em situações de demissão em massa, quando vários funcionários serão desligados simultaneamente. 

* **Método 2: Informação apenas do saldo do FGTS atualizado**

Neste método, o usuário informa apenas o valor do Saldo do FGTS Atualizado, e o programa FGTS Digital realizará automaticamente o cálculo da multa e dos juros sobre esse valor.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22149722804503)  
  
Para obter orientações detalhadas sobre os passos relativos aos MÉTODOS 1 e 2, consulte o Capítulo 4 do [Manual do FGTS](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-0-18-08-2023.pdf), intitulado **Remunerações para Fins Rescisórios**.  
  
**Saiba mais**  
Para mais informações acesse:  
- [FGTS Digital - Arquivo Simplificado para recomposição do histórico do vínculo do trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=832638360)
