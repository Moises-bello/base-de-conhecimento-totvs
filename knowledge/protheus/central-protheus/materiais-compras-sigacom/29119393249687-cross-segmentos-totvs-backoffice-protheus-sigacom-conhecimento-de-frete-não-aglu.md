---
article_id: 29119393249687
category: Materiais - Compras (SIGACOM)
content_hash: 0813403f57d96d769326a5f1fe96d23255f28fa875920d9a5c9736f3499204a8
fetched_at: '2026-06-28T22:41:16.156155+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Conhecimento de Frete
  não aglutina valores do Peso Bruto e Peso Liquido
type: support-article
updated_at: '2025-01-10T14:00:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29119393249687-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Conhecimento-de-Frete-n%C3%A3o-aglutina-valores-do-Peso-Bruto-e-Peso-Liquido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29119393231383) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Conhecimento de Frete com Pesos diferentes não Considera todos os Pesos da Nota Fiscal

**Exemplo :**

Criar os Documentos com Pesos Diferentes  
  
1. Acesse a rotina Documento de Entrada;  
2. Crie 3 notas fiscais, preenchendo os campos de Peso Bruto e Peso Líquido com valores distintos para cada uma.  
Nota 1: Peso Bruto = 90 kg; Peso Líquido = 90 kg.  
Nota 2: Peso Bruto = 140 kg; Peso Líquido = 140 kg.  
Nota 3: Peso Bruto = 180 kg; Peso Líquido = 180 kg.  
Criar o Complemento de Frete na Rotina MATA116  
  
2. Acesse a Rotina MATA116:  
Inicie o processo de criação de um Complemento de Frete.  
Vincule as Notas Criadas:  
No complemento de frete, associe as 3 notas fiscais criadas no passo anterior.  
Validar os Pesos no Documento de entrada do Complemento de Frete  
  
3. Consulte o documento gerado na rotina MATA116.  
Verifique o Comportamento dos Pesos:  
Somatória dos Pesos  
Verifique se o Peso Bruto e Peso Líquido do complemento de frete correspondem à soma dos pesos das notas vinculadas:  
Peso Bruto: 100+150+200=450 kg 100 + 150 + 200 = 450  
Peso Líquido: 90+140+180=410 kg 90 + 140 + 180 = 410

4. O complemento de frete utilizará apenas o peso do primeiro ou último documento vinculado.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão COMPRAS - Todas as Versões  
  
**Solução**

O peso líquido e bruto não serão aglutinados ao gerar a Nota Fiscal de Conhecimento de Frete. O agrupamento, neste caso, está restrito apenas aos produtos, conforme a configuração que determina se eles devem ser agrupados no documento de Conhecimento de Frete gerado. Outras informações, como duplicata, natureza e outros campos, não serão preenchidas automaticamente. Essas informações deverão ser inseridas manualmente durante a geração do conhecimento.

***Saiba Mais:***

[Página Centralizadora Compras](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
