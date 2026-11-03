---
content_hash: 4182ad8b7a697d25ae4981b0ae1e5bb6ff2d2b625ce9eb3cbefa54215ce77ee8
fetched_at: '2026-06-29T00:10:11.773657+00:00'
page_id: '453283445'
product: rm
source: tdn-rm
title: Nota Técnica 2018/005
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453283445
version: 37
---

A NT 2018.005 trouxe alterações no layout da NF-e/NFC-e e também no DANFE.

## Cronograma

Este evento entra em vigor:

* Homologação a partir de 25/02/2019
* Produção a partir de 29/04/2019.

## Legislação

Este documento foi elaborado com base na [Nota Técnica 2018.005 v1.00](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=R3JORctV9L0=) disponível no portal da NF-e.

## Implementações:

ATENÇÃO

*As implementações estão disponíveis a partir das versões 12.1.22.216 , 12.1.23.143 e 12.1.24.*  
*Em versões anteriores a 12.1.24 será necessário executar o script de marcação 12.1.22.0 (versão 12.1.22 ) ou 12.1.23.0 (versão 12.1.23) no RM.Conversor para que os campos sejam exibidos.*  
*O campo será apresentado somente para as notas que tiverem alguma informação a ser exibida e não terá efeito em notas já existentes na base antes da instalação da versão com as implementações.*

### Parametrização

* **Cadastro da Filial:** No *Cadastro → Filiais → (Selecione a Filial) → Anexos → Dados Fiscais → Dados Adicionais*, habilite o campo **HABILITA NT 2018.05** para emissão do DANFE da NF-e de acordo com  os padrões estabelecidos por esta Norma Técnica.
* **Grupo F e G (Identificação do local de Retirada e Entrega):** *Ambiente → Parâmetros → Gestão de Estoques, Compras e Faturamento → (Selecione o Movimento) → Mov - Transporte 2/3* , e marque a opção **Utilizar Endereço de Coleta e Entrega como Destinatário**.

ATENÇÃO

As alterações na NF-e destacadas neste documento terão efeito somente quando o parâmetro Habilita NT 2018.05 estiver marcado no cadastro da filial.

**Movimento:**

* **Grupo F e G (Identificação do local de Retirada e Entrega):**De acordo com a Nota Técnica 2018.005, passa a ser necessário o envio de mais dados referente ao Local de Coleta/Entrega. Existe um grupo específico para as informações de retirada (F) e um grupo específico para as informações de entrega (G). O grupo de informações de retirada será enviado se o endereço de coleta estiver preenchido e o grupo de informações de entrega será enviado se o endereço de entrega estiver preenchido.  
  Sendo assim, podem ocorrer situações em que somente os dados de coleta ou os dados de entrega estarão preenchidos.. No Movimento, em *Transporte → Coleta e Entrega*

ATENÇÃO

Até o presente momento as informações de: **CEP**, **Código do País**, **Nome do País**, **Telefone** e **E-mail** não foram implementadas pelo Nucleus, mas já estão ligadas e será gerado as tags assim que for implementado e o conteúdo for retornado pelo serviço

* **Motivo da isenção da ANVISA:** Para geração deste campo no XML:
  + - * + A flag *Controlado por Lote*, deve está habilitada no produto;
        + A flag *Produto sujeito Regulações**Sanitárias*, deve está habilitada no produto;
        + O Tipo de Movimento de entrada a flag *Consistir Lote (Item - Lote/Grade/Num)* deve está habilitada e em *Estoque - Estoque 1/3* o campo *Saldo Atual* deve ser ***Aumenta***
        + O Tipo de Movimento de saída deve*Consistir Lote*
        + ```
          O campo está localizado no cadastro do produto - Aba - integração
          ```

          ```

          ```
* **Grupo N**(Grupo CRT=1 (CSON 500)) :**** A filial deve ser optante pelo Simples Nacional

**Envio NF-e**

* **Motivo da isenção da ANVISA:** Ao enviar a NF-e a *tag***xMotivoIsencao**será gerada no grupo de medicamentos de acordo com a NT2018.005
* **Grupo ZD (Informações do Responsável Técnico):** As Informações do Responsável Técnico serão geradas em todas as NF-es Emitidas pela Filial com dados informados pela TOTVS. Para isto é necessário que seja executado o processo **Atualizar Responsável Técnico** antes de enviar a primeira NF-e ou sempre que houver alteração no credenciamento da TOTVS com a SEFAZ.

Exemplo
01111111000191
Responsável Técnico
email@totvs.com.br
31922223333
01
12ugRZOFrqQoHkWXWouMhetxfFs=
]]>ATENÇÃO

Estes dados são de responsabilidade da TOTVS e o usuário do sistema não tem a opção de alterá-los. Se for necessário atualizar, basta executar o processo **Atualizar Responsável Técnico** na tela de envio da NF-e/NFC-e.

Para habilitar a opção é necessário acessar as permissões por perfil do usuário em Serviços Globais:

O processo está presente nos processos da menu SPED(NF-e Estadual):

Se algum dado for alterado na base sem que seja pelo processo **Atualizar Responsável Técnico** as NF-e não serão enviadas apresentando a mensagem: "Falha ao inserir o grupo ZD: Os dados de responsável técnico não estão consistentes. Dica: execute o processo de atualização dos dados do responsável técnico"

* **Grupo F e G**(Identificação do local de Retirada e Entrega)**:** Tags *xNome (Razão Social)* e *IE (Inscrição Estadual)* geradas

Exemplo
22106059035
Razão Teste
Av. Raja Gabalia
1000

Raja Gabalia
3106200
Belo Horizonte
MG
122222222222212

40355886000100
Nome SOcial
Av. Cristiano Machado
400
bloco A
Sao Paulo
3106200
Belo Horizonte
MG
333333333333
]]>

* **Grupo N**(Grupo Tributação do ICMS= 60)**:**Tag referente ao valor do ICMS Próprio do Substituto cobrado em operação anterior,*vICMSSubstituto,*gerada.

Exemplo

1
60
0.00
0.0000
23.40
12.0000
2.81
]]>

* **Grupo N**(Grupo de Repasse do ICMS ST)**:**Tag *pST* referente a alíquota suportada pelo consumidor final e *vICMSSubstituto* referente ao valor do ICMS próprio do Substituto são geradas

Exemplo

1
41
57.33
12.00
6.88
6.88
0.00
0.00
]]>

* **Grupo N**(Grupo CRT=1 (CSON 500))**:**Tag referente ao valor do ICMS Próprio do Substituto cobrado em operação anterior, *vICMSSubstituto,* gerada.

Exemplo

1
500
31.85
18.00
5.73
5.73
]]>

**Consulta NF-e**

* **Mensagem de interesse da SEFAZ para o contribuinte:**Foi alterada a tela da NF-e para destacar a mensagem retornada pela SEFAZ para o contribuinte. Esta mensagem será preenchida automaticamente ao consultar a autorização da NF-e e será destacada na aba própria ao editar o cadastro.  
    
  **IMPORTANTE:** A pasta "Mensagem Interesse SEFAZ" será exibida somente se houver retorno da mensagem por parte da SEFAZ.
