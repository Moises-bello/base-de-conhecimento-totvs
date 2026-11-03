---
content_hash: a76e07fff238fc9a221eb4c1970462675234c5be2dd30f79f1eb8ed21c5117b3
fetched_at: '2026-06-29T00:05:52.719830+00:00'
page_id: '1059321682'
product: rm
source: tdn-rm
title: Gerar Movimento de Locação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1059321682
version: 8
---

![Reforma Tributária](https://tdn.totvs.com/download/attachments/1025239488/1025239500/ReformaTributaria.png)


# Geração de Movimentos

Reforma tributária
Gestão de Imóveis

]]>

3

O processo **Gerar Movimento de Locação** permite identificar e processar as baixas de locação realizadas em um período específico para a geração automática de movimentos no Backoffice.

---

## 1. Pré-requisitos e Acesso

Para utilizar esta funcionalidade, certifique-se de que as seguintes condições foram atendidas:

* **Permissão de Perfil**: Requer permissão específica nas configurações de contratos de locação, em *Serviços Globais / Perfis /**Gestão de Imóveis / Contratos de Locação / Movimento de Locação*

  + Ativar as permissões de *Gerar Movimentos de Locação, Movimentos Gerados por Pagamento e Cancelar Movimento de Locação*
* **Localização**: O processo está disponível no cadastro de contratos de locação. Tanto no menu principal em Contrato de Locação quanto em *Processos / Gerar Movimento de Locação*
* **Modo de Execução**: Pode ser executado manualmente ou via agendamento.

---

## 2. Configuração dos Parâmetros

Ao executar o processo, defina os seguintes campos na tela de parâmetros:

* **Período (Data Inicial e Final)**: Define o intervalo das baixas de locação que o sistema deve considerar.
* **Parâmetros Padrão de Movimento**: Selecione os parâmetros de movimento. A seleção é restrita à coligada do contexto atual. Para saber mais sobre estes parâmetros, consulte a documentação: [Parâmetros de Movimento de Locação (Clique Aqui)](https://tdn.totvs.com/pages/viewpage.action?pageId=1024358588)

---

## 3. Regras e Detalhes da Geração de Movimento

O sistema utiliza critérios para garantir a integridade fiscal antes de gerar os movimentos:

* **Origem das Baixas**: São considerados apenas lançamentos originados de locação cujas baixas ocorreram no período informado.
* **Tributos**: Baixas que não possuam tributos associados não serão processadas.

---

A geração segue a lógica de proporcionalidade e rastreabilidade:

1. **Proporcionalidade por Imóvel**: O sistema gera um movimento individual para cada imóvel ativo no contrato na data da execução.
2. **Cálculo de Valores**: O valor de cada movimento é calculado proporcionalmente ao percentual de participação do respectivo imóvel.
3. **Processamento em Lote**: Em execuções com múltiplos contratos, aqueles que apresentarem inconsistências serão pulados, permitindo que os demais sigam o processamento normal.
4. **Vínculo e Rastreabilidade**: Todos os movimentos gerados ficam vinculados à origem das baixas através da tabela de relacionamento `XALGCONTRATOLOCMOV`.

### Regra de geração por imóvel

A geração do movimento ocorre sempre **por imóvel**, e não apenas por contrato.

O sistema segue as seguintes regras:

#### **Contrato com apenas um imóvel:**

* Cada parcela paga gera um movimento no módulo fiscal

#### **Contrato com mais de um imóvel:**

* Cada parcela paga gera um movimento para cada imóvel, respeitando o percentual configurado no contrato

#### **Exemplo prático:**

* Valor do aluguel pago: R$ 1.000,00
* Contrato com dois imóveis

Imóvel A: 50%  
Imóvel B: 50%

#### **Movimentos gerados no módulo de faturamento:**

* Movimento do Imóvel A: R$ 500,00
* Movimento do Imóvel B: R$ 500,00

Esse rateio é realizado automaticamente com base no **percentual do imóvel definido no contrato de locação**.

---

## 5. Log de Processamento

Ao final da execução, o sistema exibirá um **log detalhado**. É fundamental revisar este log para:

* Identificar contratos processados com sucesso.
* Analisar as causas de erros ou inconsistências em contratos que não geraram movimentos.

## 6. Cancelamento de Movimentos

Após a geração dos movimentos, caso seja necessário, o sistema também permitirá o cancelamento dos movimentos gerados, desde que estejam sem nenhum bloqueio no TOTVS Gestão de Estoque, Compras e Faturamento.  
O cancelamento pode ser feito em lote, realizado através da visão de Movimentos Gerados em Contrato de Locação / Movimentos Gerados por Pagamento. É necessário ter permissão para acessar este menu, como dito no capitulo 1 deste documento.

Após acessar a visão, basta selecionar 1 ou N movimentos para serem cancelados. O cancelamento ocorrerá após a conclusão do processo.

---

## 7. Mapeamento Técnico de Campos (Banco de Dados)

### 1. Cabeçalho do Movimento (`TMOV` e `TMOVFISCAL`)

O sistema realiza o preenchimento automático da localização e competência com base nos dados do imóvel e da operação financeira.

| **Tabela** | **Campo** | **Origem da Informação** |
| --- | --- | --- |
| **TMOV** | `CODMUNSERVICO` | Código do município do endereço do imóvel. |
| **TMOV** | `CODETDMUNSERV` | UF (Estado) do endereço do imóvel. |
| **TMOV** | `CODMUNOPER` | Código do município do endereço do imóvel. |
| **TMOV** | `CODUFOPER` | UF (Estado) do endereço do imóvel. |
| **TMOVFISCAL** | `DTCOMPETENCIASERVICO` | Data da baixa do lançamento financeiro. |

---

### 2. Itens do Movimento (`TITMMOV` e `TITMMOVFISCAL`)

Define as regras fiscais e tributárias aplicadas a cada item (serviço de locação).

* **Regra Tributária (`TITMMOV.IDREGRATRIBUTARIA`)**: Preenchido com o ID da regra tributária vinculada ao contrato de locação.
* **Indicador de Operação (`TITMMOVFISCAL.CODINDOP`)**: Preenche obrigatoriamente com o valor **"020101"**.

---

### 3. Tributação (`TTRBMOV`)

A tributação dos itens segue a origem do financeiro.

* **Registros de Tributos**: Os dados de base de cálculo, alíquota e valor devem ser inseridos de acordo com a tabela de tributos da baixa financeira (`FLANBAIXATRB`).

---

### 4. Dados do Destinatário do Serviço (`TMOVFISCAL`)

Informações extraídas diretamente do cliente vinculado ao lançamento financeiro baixado.

* **NOMEDESTSERV**: Nome/Razão Social do cliente do lançamento financeiro.
* **CNPJCPFDESTSERV**: CNPJ ou CPF do cliente do lançamento financeiro.
* **Outros Campos**: Preencher com os demais dados cadastrais de endereço e contato do destinatário do serviço.

---

### 5. Dados Complementares do Imóvel (`TMOVFISCALSERV`)

Este bloco detalha a localização física e identificação municipal do imóvel locado.

| **Campo** | **Origem / Regra** |
| --- | --- |
| **CIB** | CIB (Cadastro Imobiliário Brasileiro) do Imóvel. |
| **INSCRICAOIMOBILIARIA** | Inscrição municipal do imóvel. |
| **CEPENDIMOVEL** | CEP do endereço do imóvel. |
| **ENDIMOVELBAIRRO** | Bairro do endereço do imóvel. |
| **ENDIMOVELCODETD** | Estado (UF) do endereço do imóvel. |
| **ENDIMOVELCODMUNICIPIO** | Código do município do endereço do imóvel. |
| **ENDIMOVELCOMPLEMENTO** | Complemento do endereço do imóvel. |
| **ENDIMOVELLOGRADOURO** | Logradouro do endereço do imóvel. |
| **ENDIMOVELNUMERO** | Número do endereço do imóvel. |
| **Campos Exterior (EXT)** | Preencher `CEP`, `Cidade` e `Região` somente se o imóvel estiver localizado fora do Brasil. |
