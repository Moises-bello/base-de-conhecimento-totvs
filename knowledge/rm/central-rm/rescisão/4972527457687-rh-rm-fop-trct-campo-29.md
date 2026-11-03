---
article_id: 4972527457687
category: Rescisão
content_hash: 40eb18953e6a23ac3864211581dbbb7afeb1fd2ffcbcfcc33ef22dd7008b461e
fetched_at: '2026-06-28T22:46:54.396913+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: campo 29'
type: support-article
updated_at: '2025-01-20T14:09:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4972527457687-RH-RM-FOP-TRCT-campo-29
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:48 min** **Dúvida**Como realizar a parametrização do Campo 29- Pensão Alimentícia (%) FGTS?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, segue abaixo orientações:  
  
Primeiramente, é importante ressaltar que o campo 29 do Termo de Rescisão de Contrato de Trabalho é calculado através de fórmula. Portanto, deve ser criada uma fórmula para calcular o percentual e informá-la no campo **Fórmula Pensão Alimentícia (%) FGTS (Campo 29)**. Esse campo está localizado em: **Rescisão | TRCT | Portaria 1621\2010**. Veja:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4991955866135/mceclip0.png)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4972592384279/mceclip5.png)  
  
Para a criação da fórmula, siga os passos abaixo:  
  
1. Acesse: **Administração de Pessoal | Fórmulas.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4971393389079/mceclip0.png)**  
  
2. Clique no ícone **Incluir** para adicionar uma nova fórmula ou edite uma fórmula pré-cadastrada.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4971499325335/mceclip1.png)  
  
Abaixo um exemplo de fórmula que pode ser utilizada:  
  
Código: CHAPA  
Titulo: CHAPA  
Texto: CHAPA  
  
![](https://v2uploads.zopim.io/3/Y/h/3YhhAljRQojs3mXfAHLtQZRLS5ueXJam/a5806f1a1de580af3baeec70ff11e7d07cb504da.png)  
  
Cadastre a consulta SQL abaixo:  
  
Código: Campo29  
Titulo: Campo29  
Texto: SELECT SUM(PERCENTUAL) FROM PFDEPEND WHERE CHAPA =:FRM\_CHAPA  
  
![](https://v2uploads.zopim.io/3/Y/h/3YhhAljRQojs3mXfAHLtQZRLS5ueXJam/3dad05be0158971a19091c3f7d36fe01aed1a31a.png)   
  
Cadastre a fórmula abaixo:  
  
Código: CAMPO29  
Titulo: CAMPO29  
Texto: EXECSQL('CAMPO29'); RESULTSQL('CAMPO29','Column1')   
  
![](https://v2uploads.zopim.io/3/Y/h/3YhhAljRQojs3mXfAHLtQZRLS5ueXJam/8c0a70959efc3bb7a7a0e501a19e3d72628a8dbe.png)  
  
3. Após criar a fórmula, salve o registro e selecione a fórmula criada no **Campo 29-Fórmula Pensão Alimentícia (%) FGTS** no momento da geração do TRCT.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4972189070615/mceclip4.png)  
  
4. Logo, gere o relatório normalmente.  
  
**Importante**A fórmula exemplificada neste artigo é apenas um exemplo. Portanto, fica a cargo da empresa personalizar a fórmula, a fim de que contempla o que deseja. Lembrando que, o Suporte padrão não presta auxílio na criação ou manutenção de fórmulas. Para a criação de outra fórmula, será necessário verificar internamente com sua equipe de TI se é possível realizar a criação da fórmula necessária ou contratar nossa Equipe de Consultoria.
