---
article_id: 4403859340951
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5d43c2d8bb98b6629d7c4c68171209dbcdd19559b8c389c266bd2a3cdbc0f406
fetched_at: '2026-06-28T22:38:57.080081+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA265 - Protheus
  se perde na geração da série dos produtos
type: support-article
updated_at: '2021-07-13T11:01:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403859340951-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA265-Protheus-se-perde-na-gera%C3%A7%C3%A3o-da-s%C3%A9rie-dos-produtos
---

**Dúvida**Na rotina MATA265, no botão "Outras ações" existe a opção de Gerar Número de Série. porém o resultado não está correto. Quando tem letras na série inicial o sistema se perde. Como corrigir

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**A serialização padrão do Protheus envolve números e letras.  Vamos exemplificar abaixo:

**Iniciando o Número de Série com "1":**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403859068823/mceclip0.png)

Neste primeiro exemplo, verificamos que iniciamos os números de serie com o numeral 1, desta forma o sistema vai preencher todas as possibilidades, sendo do 1 ao 9 para começar a preencher com as letras, quando as possibilidades esgotam e teoricamente viraria de 9 para 10:

**Iniciando o Número de Série com "01":**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403860764183/mceclip1.png)**

Nesse segundo exemplo a geração inicia em "01", neste caso o Sistema vai seguir essa sequencia até atingir o número 99​, que seria a ultima possibilidade dentro deste range.

**Gostaria que o range mudasse por exemplo de 99 para 100, ou 09 para 10. O que fazer?**

Uma alternativa paliativa seria o uso do ponto de entrada **MA265TDOK ([clique aqui para detalhes](https://tdn.totvs.com/pages/releaseview.action?pageId=6087623)).** É interessante validar se o Ponto de Entrada atenderá à necessidade na serialização.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
