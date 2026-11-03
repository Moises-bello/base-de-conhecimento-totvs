---
article_id: 360052701353
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 7b9fd191e6f731af0808470eca3a0ee90a879cf3875690ba34ad0af0776f1fe5
fetched_at: '2026-06-28T22:42:11.846626+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Registro Tipo
  26 – Resumo da Apuração dos Créditos
type: support-article
updated_at: '2022-08-18T14:08:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052701353-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Registro-Tipo-26-Resumo-da-Apura%C3%A7%C3%A3o-dos-Cr%C3%A9ditos
---

**Dúvida**  
Registro tipo 26 – Resumo da apuração dos créditos  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Registro tipo 26 – Resumo da apuração dos créditos

Tem como base as informações contidas na apuração do ICMS do período.  
  
A partir da referência maio de 2009 (entrega até 10/06/09) foram feitas adequações relacionadas às novas validações da DIME e DCIP. O validador da DIME passou a criticar alguns CFOPs, visto que não dão direito ao crédito pelas entradas (movimentações de imobilizado, material de uso e consumo, etc.) para os quais ou não é permitido crédito ou existe campo específico para ser lançado, em Outros créditos ou na DCIP, por exemplo.  
  
Para as seguintes operações não é permitida a escrituração do crédito do ICMS no livro registro de entradas:  
  
I - Créditos e ressarcimentos de ICMS (exemplo: 1.601, 1.602, 1.603, 1.605, 2.603);  
II - Operações com bens de ativo imobilizado (exemplo: 1.406, 1.551, 1.552, 1.553, 1.554, 1.555, 1.604, 2.406, 2.551, 2.552, 2.553, 2.554, 2.555, 3.551, 3.553);  
III - Entradas ou aquisições de serviços do exterior (exemplo: 3.101, 3.102, 3.126, 3.127, 3.201, 3.202, 3.205, 3.206, 3.207, 3.211, 3.251, 3.301, 3.351, 3.352, 3.353, 3.354, 3.355, 3.356, 3.556, 3.651, 3.652, 3.653, 3.949);  
IV - Operações com material para uso ou consumo (exemplo: 1.407, 1.556, 1.557, 2.407, 2.556, 2.557).  
  
No item Crítica de CFOP no Validador da DIME e Controle na DCIP do Crédito por Pagamento Antecipado, disponibilizado pelo site da Sefaz-SC, estão relacionados todos os CFOPs de cada uma das operações anteriores.  
  
Portanto, não é permitido que notas fiscais com os CFOPs relacionados tenham em sua escrituração valor de ICMS a creditar. Esses documentos não podem ser lançados com escrituração na coluna Tributados do Livro Fiscal.  
  
Caso algum documento seja lançado com algum desses CFOPs e com valor de crédito de ICMS, a seguinte rejeição será apresentada: Registro 26 Item 020 - Valor do item não pode ser maior que o item 030 do quadro 03 deduzidos os eventuais créditos.

Para a geração de algumas das informações requeridas no Registro Tipo 26 (Resumo da Apuração dos Créditos), é necessário incluir alguns códigos manualmente para alguns itens, conforme segue:

Em Outros Créditos:

26030 - Crédito de ativo permanente.  
26040 - Crédito por diferencial de alíquota de material de uso e consumo.  
26050 - Crédito de ICMS retido por substituição tributária.  
26100 - Crédito relativo a operações de importação.  
26110 - Crédito relativo à aquisição de atacadistas de outras UFs.  
26120 - Créditos por responsabilidades tributárias.  
26130 - Outros pagamentos devidos por ocasião do fato gerador.  
26140 - Total de créditos por regime especial.  
26150 - Restituição de ICMS.  
  
Observação:

O código de subitem 26140 deve ter, nas 15 posições iniciais de sua descrição, o número de identificação do regime especial. Esse número alimenta automaticamente o registro 46 (Créditos por regimes e autorizações especiais). Esse item deve ser informado apenas para preenchimento automático do registro 46, pois o registro 26 item 140 não deve ser preenchido a partir do período de referência abril de 2008.

Exemplo:

![image2016-4-25 17:43:55.png](https://tdn.totvs.com/download/attachments/224114798/image2016-4-25%2017%3A43%3A55.png?version=1&modificationDate=1461613558000&api=v2)

No exemplo acima, observe que é possível inserir mais de um protocolo para o mesmo período; basta contemplar um sequencial ao final do código de subitem, como é o registro 26140, que possui 1 e 2 ao seu final.

Abaixo link contendo informações na integra referente a geração da DIME SC:  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=224114798>
