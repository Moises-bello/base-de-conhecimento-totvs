---
article_id: 360018112091
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 4991a8684465ffa65e25560d2b50822e5af0a483a963c3e2144d5d6f1709c816
fetched_at: '2026-06-28T22:42:06.706950+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal/
  EFD Contribuições - Como alterar o produto no Registro 0205 pelo Ponto de Entrada
  SPED0205 (ALTERAÇÃO DO ITEM)
type: support-article
updated_at: '2023-01-25T18:16:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018112091-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-EFD-Contribui%C3%A7%C3%B5es-Como-alterar-o-produto-no-Registro-0205-pelo-Ponto-de-Entrada-SPED0205-ALTERA%C3%87%C3%83O-DO-ITEM
---

**Dúvida**Como alterar o produto no registro **0205** do arquivo magnético **SPED FISCAL** ou arquivo magnético **EFD Contribuições** utilizando o Ponto de Entrada **SPED0205**?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**Este registro é gerado com base no histórico de alterações do produto, armazenadas na **tabela AIF**.

Não é mais permitido informar no mesmo registro **0205** as informações de Descrição Anterior e Código Anterior, **campos 02 e 05** respectivamente. Por este motivo serão gerados dois registros **0205**, onde um registro terá o campo de Descrição Anterior preenchido e Código Anterior vazio, e outro registro **0205** com o **campo de Descrição Anterior vazio e Código Anterior preenchido**. Desta forma a rotina continua gerando as mesmas informações (Descrição Anterior e Código Anterior) considerando a nova regra de validação do **0205**.

Para solucionar essa dúvida, realize os seguintes passos:  
1. Configure os parâmetros **MV\_HISTTAB** igual .T. e **MV\_DTINCB1** igual **B1\_DATREF**.

2. Este registro somente é gerado no momento da alteração cadastral do produto, alimentando tabela **AIF**.  A data considerada para alteração é a data computador.

3. Realize a geração do arquivo magnético **SPEDFISCAL** ou arquivo magnético do **EFD Contribuições**.

**Importante**  
Registro pode ser gerado por meio do Ponto de Entrada **SPED0205** (**Geração do registro 0205 do SPED Fiscal**):   
*Link:* <https://tdn.totvs.com/pages/releaseview.action?pageId=706921537>  
  
Caso não exista os parâmetros citado acima, segue configuração para criação:  
Registros de histórico de alterações cadastrais (**0175 e 0205**) Itens/Pastas Descrição:  
**MV\_HISTTAB  
Tipo : Lógico**  
**Descrição :  <definido pelo cliente> Valor Padrão Habilita (.T.) ou desabilita (.F.) o histórico das alterações do cadastro de clientes/fornecedores/transportadoras e produtos.**  
**Conteúdo: .T.**  
  
**Registro Tipo 0200 – Identificação do Item Itens/Pastas Descrição:**  
**MV\_DTINCB1  
Tipo : Caracter**  
**Descrição <definido pelo cliente> Valor Padrão Determina a rotina qual o campo da tabela SB1 que contém a data de cadastro (inclusão) do produto no sistema.**  
**Default: O conteúdo default deste parâmetro é o campo B1\_DATREF.**
