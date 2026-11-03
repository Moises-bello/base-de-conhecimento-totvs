---
content_hash: f1bd04a7cc21c45f1571b3226127322bf001d1785f3e1530423104bf97e0116d
fetched_at: '2026-06-29T00:10:47.689709+00:00'
page_id: '560653354'
product: rm
source: tdn-rm
title: Dados do prestador de serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653354
version: 16
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **prestador** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | **G** | **1-1** | **Tag ráiz para as informações sobre o prestador.** |  |  |
| inscmun | prestador | E | 1-1 | Inscrição municipal do prestador. | GFILIAL.INSCMUN | Inscrição Municipal do prestador do serviço cadastrada na Filial do RM.  Para manter a máscara da inscrição municipal é necessário marcar a opção de "Não Remover Máscara IM Prestador" nos [dados fiscais do município.](https://tdn.totvs.com/pages/viewpage.action?pageId=652399054) |
| cpfcnpj | prestador | E | 1-1 | CPF/CNPJ do prestador. | GFILIAL.CGC |  |
| razao | prestador | E | 1-1 | Razão social do prestador. | GFILIAL.NOME |  |
| fantasia | prestador | E | 1-1 | Nome fantasia do prestador. | GFILIAL.NOMEFANTASIA |  |
| codmunibge | prestador | E | 0-1 | Código do município do prestador padrão IBGE |  | Código de Classificação definido para o município conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI) |
| codmunsiafi | prestador | E | 0-1 | Codigo do município do prestador padrão SIAFI |  | Código de Classificação definido para o município conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI) |
| cidade | prestador | E | 0-1 | Nome da cidade do prestador. | GMUNICIPIO.NOMEMUNICIPIO |  |
| uf | prestador | E | 1-1 | Unidade federativa do prestador. | GFILIAL.ESTADO |  |
| email | prestador | E | 0-1 | Endereço de e-mail do prestador. | GFILIAL.EMAIL |  |
| ddd | prestador | E | 0-1 | DDD do telefone do prestador. | GFILIAL.DDD |  |
| telefone | prestador | E | 0-1 | Telefone do prestador. | GFILIAL.TELEFONE |  |
| simpnac | prestador | E | 0-1 | Optante pelo regime simples nacional. Os conteúdos possíveis são:  •  1 – Sim;  •  2 – Não. | DFILIAL.OPTANTESIMPLES | Se DFILIAL.OPTANTESIMPLES > 0 Entao Sim Senao Não |
| dtinisi | prestador | E | 0-1 | Data início Simples Nacional. |  | Não será gerado. |
| incentcult | prestador | E | 0-1 | Incentivador cultural. Os conteúdos possíveis são:  •  1 – Sim;  •  2 – Não. | TMOVCOMPL.INCENTIVCULTURAL | Se TMOVCOMPL.INCENTIVCULTURAL Preenchido Entao Sim Senao Não |
| numproc | prestador | E | 0-1 | Número do processo judicial ou administrativo de  suspensão da exigibilidade | DPROCESSOJUDICIAL.NUMERO | Processo Judicial ou Administrativo Vinculado |
| logradouro | prestador | E | 1-1 | Descrição do logradouro do prestador. | GFILIAL.RUA |  |
| numend | prestador | E | 1-1 | Numero do endereço do prestador. | GFILIAL.NUMERO |  |
| compleend | prestador | E | 0-1 | Complemento do endereço do prestador. | GFILIAL.COMPLEMENTO |  |
| bairro | prestador | E | 1-1 | Nome do bairro do prestador. | GFILIAL.BAIRRO |  |
| tplogradouro | prestador | E | 0-1 | Tipo de logradouro.  Os valores válidos são:  •  1 – Avenida;  •  2 – Rua;  •  3 – Rodovia;  •  4 – Ruela;  •  5 – Rio;  •  6 – Sítio;  •  7 – Sup Quadra;  •  8 – Travessa;  •  9 – Vale;  •  10 – Via;  •  11 – Viaduto;  •  12 – Viela;  •  13 – Vila  •  14 – Vargem. | DTIPORUA.DESCRICAO | Será verificado se DTIPORUA.DESCRICAO coincide com algum item da lista ao lado |
| tpbairro | prestador | E | 0-1 | Tipo de bairro.  Os valores válidos são: •  1 – Bairro;  •  2 – Bosque;  •  3 – Chácara;  •  4 – Conjunto;  •  5 – Desmembramento;  •  6 – Distrito;  •  7 – Favela;  •  8 – Fazenda;  •  9 – Gleba;  •  10 – Horto;  •  11 – Jardim;  •  12 – Loteamento;  •  13 – Núcleo;  •  14 – Parque;  •  15 – Residencial;  •  16 – Sitio;  •  17 – Tropical;  •  18 – Vila;  •  19 – Zona. | DTIPOBAIRRO.DESCRICAO | Será verificado se DTIPOBAIRRO.DESCRICAO coincide com algum item da lista ao lado |
| cep | prestador | E | 1-1 | CEP do prestador. | GFILIAL.CEP |  |
| regApTribSN | prestador | E | 0-1 | Regime Apuração Simples Nacional. | DFILIAL.SUBLIMITEEXCEDIDO | Este campo só é gerado caso a Filial esteja configurada como Optante Regime Simplificado.  Se opção "Sublimite excedido" estiver marcada o campo é gerado com 2  Se estiver desmarcada é gerado com 1  As outras opções não serão geradas. |
| RegApurSimp | prestador | E | 0-1 | Regime Apuração Simplificada. | DFILIAL.SUBLIMITEEXCEDIDO | Este campo só é gerado caso a Filial esteja configurada como Optante Regime Simplificado.  Se opção "Sublimite excedido" estiver marcada o campo é gerado com 2  Se estiver desmarcada é gerado com 1  As outras opções não serão geradas. |
