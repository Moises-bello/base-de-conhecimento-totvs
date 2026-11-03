---
article_id: 360025553913
category: Escrita Fiscal - Impostos - ICMS
content_hash: 95473ff781c9823f92c24fda2fb8197c4648dd777fae42e7fda0a1276c7caa45
fetched_at: '2026-06-28T22:39:25.991305+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Preenchimento dos
  dados da DI no Modulo Livros Fiscais
type: support-article
updated_at: '2021-07-28T16:42:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025553913-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Preenchimento-dos-dados-da-DI-no-Modulo-Livros-Fiscais
---

**Dúvida**  
Preenchimento dos dados da DI no Modulo Livros Fiscais  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Notas de importação para clientes que utilizam o modulo de Materiais e parâmetro MV\_EASY= Não

Para preencher os dados da DI , entrar em (livros fiscais ->movimentos->nf manual de entrada->ações relacionadas->complemento->importação e depois preencher os seguintes campos:

Dados da DI

Campos obrigatórios para NFe:

CD5\_NDI - Número do Documento de Importação (DI/DSI/DA/DIRE)

CD5\_DTDI - Data de Registro da DI/DSI/DA/DIRE

CD5\_LOCDES - Local de desembaraço

CD5\_UFDES - Sigla da UF onde ocorreu o Desembaraço Aduaneiro

CD5\_DTDES - Data do Desembaraço Aduaneiro

CD5\_CODEXP - Código do exportador

CD5\_NADIC - Numero da adição

CD5\_SQADIC - Numero seqüencial do item dentro da adição

CD5\_CODFAB - Código do fabricante Estrangeiro

CD5\_BCIMP - Valor da Base de Cálculo do Imposto de importação(mesmo zerado)

CD5\_VLRII - Valor Imposto de Importação(mesmo zerado)

CD5\_VTRANS - tpViaTransp

CD5\_INTERM - tpIntermedio

CD5\_UFTERC – UFTerceiro

CD5\_ACDRAW – Drawback – caso não use deixar em branco.

Para habilitar a tela de importação/exportação o sistema faz a seguinte validação.

Neste caso por favor rever todos os campos abaixo, pois se não habilitar a tela é devido o campo TIPO estar = Jurídico.

Como deverá constar o cadastro do cliente/fornecedor caso seja do EXTERIOR/EXPORTAÇÃO/IMPORTAÇÃO

- Bairro pode ser informado qualquer um, pois essa validação não é feita. Contudo, é uma informação obrigatória.   
- Inscrição Estadual e CNPJ não são obrigatórios para transmissão do SEFAZ, poderão ficar em branco.  
- Código de Município deve ser preenchido com 99999. Você pode incluir o código de município 99999 diretamente na tabela CC2 (tabela de municípios do IBGE)

Formulário próprio = SIM

Cadastro de fornecedor/ cliente = EX  
- Estado = EX  
- CEP = 00000000  
- Tipo= X=Outros  
- CODIGO PAIS (A1\_PAIS) DEVE SER DIFERENTE DE BRANCO E 01058
