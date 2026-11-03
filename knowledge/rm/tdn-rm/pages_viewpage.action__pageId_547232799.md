---
content_hash: 0e2675eb55d79eaa238a362833731747da56a218bd1e6f9885943a44ff011280
fetched_at: '2026-06-29T00:10:42.265607+00:00'
page_id: '547232799'
product: rm
source: tdn-rm
title: Alterações ECF 2020 - Layout 6
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547232799
version: 22
---

nonefalse

O Layout 6 da Escrituração Contábil Fiscal - ECF foi introduzido pelo [Ato Declaratório Cofis no 70/2019](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=105592&visao=anotado), e deve ser utilizado para transmitir as situações normais de 2019 e situações especiais de 2020.

**Registro 0000: Abertura do Arquivo Digital e Identificação da Pessoa Jurídica**

O campo 3 - COD\_VER (Código da versão do leiaute) de acordo com o layout 6, para o ano-calendário 2019 e situações especiais de 2020, o leiaute a ser informado deverá ser = 0006.

Exemplo de visão de dadosImportante

* Para gerar o Layout atualizado deve-se selecionar no *Processo do Gerador de Saídas* a versão 006 (ou mais atual).

### **Registro 0930: Identificação dos Signatários da ECF**

VisaoDeDadosRegistro 0930

| N° | Campo | Descrição | Tipo | Tamanho | Decimal | Valores Válidos | Obrigatório |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | IDENT\_NOM | Texto fixo contendo a identificação do registro (0930). | C | 4 | - | [0930] | Sim |
| 2 | IDENT\_NOM | Nome do Signatário | C | - | - | - | Sim |
| 3 | IDENT\_CPF\_CNPJ | CPF/CNPJ: O tamanho do campo deve ser exatamente o informado na coluna “Tamanho”. | N | CPF (11) CNPJ(14 | - | - | Sim |
| 4 | IDENT\_QUALIF | Código de qualificação do assinante, conforme tabela do Sped (Disponibilizada no programa da ECF no diretório Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas/SPEDECF\_LOCAL$SPEDECF\_QUALIF\_ASSINANTE). | C | 3 | - | - | Sim |
| 5 | IND\_CRC | Número de inscrição do contabilista no Conselho Regional de Contabilidade. | C | - | - | - | Sim |
| 6 | EMAIL | E-mail do signatário | C | 60 | - | - | Sim |
| 7 | FONE | DDD e telefone do signatário | C | 14 | - | - | Sim |

O Registro 0930 tem como objetivo informar os dados dos signatários da escrituração.

Para atender a obrigatoriedade foi criada a flag **"Segunda Assinatura - Própria Empresa"** caso seja necessário informar a segunda assinatura da ECF com os dados da própria empresa, que é a Filial Matriz.

O campo pode ser acesso através do cadastro da Filial | Anexos | Parâmetros ECF - Escrituração Contábil Fiscal | pasta Complementares.

O campo **"Código da Qualificação do Assinante"** só será habilitado caso a flag "Segunda Assinatura - Própria Empresa" estiver **marcada**.

O Código da Qualificação do Assinante é a mesma listagem que já existe no cadastro Representante do cadastro da Filial.

Imagem 1Imagem 2Importante

Por default o parâmetro permanece desmarcado.

Código de Qualificação do Assinante

| Código | Descrição 1 |
| --- | --- |
| 203 | Diretor |
| 204 | Conselheiro de Administração |
| 205 | Administrador |
| 206 | Administrador do Grupo |
| 207 | Administrador de Sociedade Filiada |
| 220 | Administrador Judicial – Pessoa Física |
| 222 | Administrador Judicial – Pessoa Jurídica - Profissional Responsável |
| 223 | Administrador Judicial/Gestor |
| 226 | Gestor Judicial |
| 309 | Procurador |
| 312 | Inventariante |
| 313 | Liquidante |
| 315 | Interventor |
| 401 | Titular Pessoa Física - EIRELI |
| 801 | Empresário |
| 900 | Contador |
| 900 | Contabilista |
| 999 | Outros |

**Registro L210: Informativo da Composição de Custos**

De acordo com o layout atual (versão 6), foi alterada a geração do campo 4-VALOR (Saldo Final da Conta de Custos Antes do Encerramento), que passa a gerar valores com sinal negativo  e valores positivos sem sinal.

Exemplo de relatório

**Registro Y600: Identificação e Remuneração de Sócios, Titulares, Dirigentes e Conselheiro**

Para atender a alteração do campo 8 - Qualificação do Sócio, Titular, Dirigente ou Conselheiro do registro Y600, foi acrescentada a opção “**18 – Usufrutuário de Quotas ou Ações**” enumerado do campo “**Qualificação**”.

O campo pode ser acessado através do cadastro da Filial | Anexos | Parâmetros ECF - Escrituração Contábil Fiscal | Anexos | Sócio.

TabelaDinamicaImagem 1Imagem 2REGISTRO 0020

**REGISTRO 0020:**

No Manual 006 os valores válidos para o campo “IND\_ALIQ\_CSLL” do registro 0020, passaram a ser: 1 – 9%; 3 – 20%; 4 – 15%. Até o Manual 005 os valores aceitos eram: 1 – 9%; 2 – 17%; 3 – 20%.

Efetuamos o tratamento na geração do registro, para considerar as alíquotas válidas de acordo com o Layout que está sendo utilizado.  
  
Lembrando que a alíquota pertinente deve ser preenchida na pasta detalhamento do período de apuração do CSLL:

**Observação:** Caso seja realizada geração do arquivo com versão do layout que não corresponde à alíquota preenchida, o campo “IND\_ALIQ\_CSLL” ficará vazio
