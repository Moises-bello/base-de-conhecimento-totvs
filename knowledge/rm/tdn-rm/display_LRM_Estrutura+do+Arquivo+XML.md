---
content_hash: 3acd97d5afecfa567d3e1099380bab58711066abf6d6e57bca8cc51cae9aa315
fetched_at: '2026-06-29T00:10:03.812511+00:00'
page_id: '452719158'
product: rm
source: tdn-rm
title: Estrutura do Arquivo XML
type: documentation
url: https://tdn.totvs.com/display/LRM/Estrutura+do+Arquivo+XML
version: 1
---

**Estrutura do Arquivo XML**

---

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |
| **Campo** | **Descrição** | **Tamanho Máximo** | **Tipo** | **Obrigatório** | **Informações** |  |
| IDLOTE | Identificador do Lote | 10 | N | Sim |  |  |
| CA | Certificado de Aprovação | 30 | C | Não |  |  |
| DTAQUISICAO | Data de Aquisição | 10 | D | Não | Formato: dd/MM/aaaa |  |
| DTVALIDADE | Data de Validade | 10 | D | Não | Formato: dd/MM/aaaa |  |
| DTDURABILIDADE | Data de Durabilidade | 10 | D | Não | Formato: dd/MM/aaaa |  |
| DTVALIDADECA | Data de Validade do CA | 10 | D | Não | Formato: dd/MM/aaaa |  |
| DURABILIDADE | Durabilidade | 5 | N | Não |  |  |
| CRI | Certificado de Registro do Importador | 30 | C | Não |  |  |
| CRF | Certificado de Registro do Fabricante | 30 | C | Não |  |  |
| FABRICANTE | Nome do Fabricante | 100 | C | Não |  |  |
| OBSERVACOES | Observações | 4000 | C | Não |  |  |
| HIGIENIZADO | Higienizado | 1 | C | Não | Valor S para Sim ou valor N para Não |  |
| INVALIDO | Inválido | 1 | C | Não | Valor S para Sim ou valor N para Não |  |
| CODFILIAL | Código da Filial | 2 | N | Não |  |  |
| CODSECAO | Código da Seção | 35 | C | Não |  |  |
| QUANTIDADE | Quantidade a ser lançada | 5 | N | Sim |  |  |
|  |  |  |  |  |  |  |
| **Tipo:** |  |  |  |  |  |  |
| C -> Caracter |  |  |  |  |  |  |
| D -> Data |  |  |  |  |  |  |
| N -> Numérico |  |  |  |  |  |  |
