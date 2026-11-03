---
article_id: 360046503773
category: Encargos
content_hash: cf91745024f3d6fe6e34ac3a35c07d7199890add9865fc1a536842a71397b09b
fetched_at: '2026-06-28T22:46:53.319948+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RM - FOP - Portaria 139/2020 - Recolher as Contribuições Segurados e Outras
  Entidades(terceiros)
type: support-article
updated_at: '2023-04-03T15:00:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046503773-RM-FOP-Portaria-139-2020-Recolher-as-Contribui%C3%A7%C3%B5es-Segurados-e-Outras-Entidades-terceiros
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**: 00:02:30 min**

**Dúvida**  
Como realizar o recolhimento das Contribuições Segurados e Outras Entidades (terceiros) sem considerar a parte Previdenciária Patronal e Acidente de Trabalho ?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
**Importante:** Será necessário a geração de duas Guias de Inss e Lançamento Financeiros, uma para recolhimento atual(Segurados e Outras entidades e) e outra para recolhimento futuro ( Patronal e Acidente de Trabalho).  
  
**1.** No modulo RH acesse **Folha de pagamento| Encargos| Guia de INSS | Guia** **Parâmetros | Percentuais para cálculo,** Campo **%Empresa** e preencha o campo com 0,00.![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067958914/mceclip3.png)  
  
**2.** Caso utilize os **Parâmetros da Coligada** na geração da Guia de INSS, também deverá preencher o campo **%Empresa** com 0,00, conforme imagem abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065936953/mceclip0.png)  
  
**Importante:** A Guia de Inss deverá ser gerada com a **Quebra por CNPJ- Filial**

**3.**Acesse a aba Lançamento Financeiro e marque o parâmetro **Gera lançamentos financeiros** e informe o lançamento de INSS Folha, preencha os campos Data de Emissão e Data de Vencimento e **Execute**.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067991994/mceclip0.png)

**4.** Após clicar em **Executar** acesse a aba  **Valores da Seção** o campo **% Empresa** estará zerado mantendo os valores de **Segurados e Terceiros**.

Deverá zerar os valores de **Acidente de Trabalho** e depois clicar em **recalcular valores**

Com esta parametrização será feito o recolhimento parte Segurado e Outras Entidades (terceiros) , tanto na GPS quanto para o Lançamento Financeiro INSS.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067992154/mceclip1.png)  
  
**Fonte:** [Portaria ME nº139/2020](http://www.in.gov.br/en/web/dou/-/portaria-n-139-de-3-de-abril-de-2020-251138204)  
**Saiba Mais:**[Centralizadora Medidas Provisórias](https://tdn.totvs.com/pages/releaseview.action?pageId=544709221)
