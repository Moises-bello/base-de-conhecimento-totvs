---
article_id: 360016257791
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: f41501231594b77857d766af1588fb63683326657d57988fdb13f0c01b2be471
fetched_at: '2026-06-28T22:42:05.328585+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  Bloco C: Escrituração Individualizada x Consolidada no arquivo txt'
type: support-article
updated_at: '2023-06-06T15:46:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016257791-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Bloco-C-Escritura%C3%A7%C3%A3o-Individualizada-x-Consolidada-no-arquivo-txt
---

**Dúvida**1- Como escriturar as notas fiscais de forma **individualizada** gerando os registros C100 e C170?  
2- Como escriturar as notas fiscais de forma **consolidada** gerando os registros C180/ C190 e filhos?  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**Para solucionar as dúvidas acima, verifique as orientações:  
  
1. **Registro C100:** Documento - Nota Fiscal (Código 01), Nota Fiscal Avulsa (Código 1B), Nota Fiscal de Produtor (Código 04), NF-e (Código 55) e NFC-e (Código 65).

Para escriturar as notas fiscais de forma individualizada gerando os registros C100/C170, preencha a pergunta "**Indicador Nfe/Cupom? 2- Individ.**" na wizard da geração do arquivo.

![TESTEGIF2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360011962892/TESTEGIF2.gif)

2. **Registro C180/ C190 e filhos:** Consolidação de Notas Fiscais Eletrônicas Emitidas Pela Pessoa Jurídica (Códigos 55 e 65) – Operações de Vendas.

Para escriturar as notas fiscais de forma consolidada gerando o registro C180, preencha a pergunta "I**ndicador Nfe/Cupom? 1- Consolidado**" na wizard da geração do arquivo.

![TESTEGIF1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360011962912/TESTEGIF1.gif)
