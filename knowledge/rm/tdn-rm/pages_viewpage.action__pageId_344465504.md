---
content_hash: 4f78aece38422b79cc6964e7b7911b0cf5c4ce66dafe77f00025223d3d4a4556
fetched_at: '2026-06-29T00:08:53.264523+00:00'
page_id: '344465504'
product: rm
source: tdn-rm
title: Como_Fazer_Aluguel_Despesas do Imóvel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344465504
version: 6
---

|  |  |
| --- | --- |
| **Produto:** | TOTVS Incorporação |
| **Versões:** | 12.1.6 |
| **Ocorrência:** | N/A |
| **Ambiente:** | RM |
| **Passo a passo:** | N/A |
| **Observações:** | N/A |

# Objetivo

Explicaremos neste documento como utilizar o recurso de Evento Financeiro, do módulo de Aluguel,  para lançamento de Despesas de um Imóvel, como por exemplo:

* IPTU
* Taxa de Incêndio
* Taxa de Condomínio

As despesas acima mencionadas são em geral despesas anuais recorrentes e são repassadas ao locatário (inquilino) de um contrato de locação, mas também podem ser lançadas como Evento Financeiro do Aluguel despesas eventuais, como uma reforma.

Abaixo descreveremos alguns exemplos aplicados e como parametrizá-los.

# Definição da Regra de Negócio

### IPTU

O Imposto Territorial Urbano - IPTU, é uma despesa do proprietário do Imóvel, mas é permitida a transferência da cobrança para o locatário quando houver um contrato de locação que regulamente esta transferência de obrigação.

**Caso 1. Quanto o Imóvel é de Terceiro e não está Alugado (Vacância)**

Quando o imóvel **não** pertence a Administradora (imobiliária), o IPTU pode ser repassado para o proprietário.

Para isso é necessário que:

1. No cadastro do Imóvel deixe a opção *"Imóvel de propriedade da *administradora*de Imóvel?*" DESMARCADA indicado assim que este imóvel é de propriedade de Terceiros;
2. O Imóvel deve estar associado a um Contrato de Administração efetivado;
3. Ao criar o Evento financeiro deve ser informado o Contrato de Administração e indicar que haverá repasse ao Locador;  
     
     
     
   1. O repasse deve ser feito através de um Evento Avulso.   
        
        
      Quando informar que o evento é **"Avulso"** o sistema permitirá a geração de um novo lançamento financeiro, mas a geração não é automática, sendo necessário que depois de salvar acesse o menu Processos→ "Incluir Lançamento Financeiro".

**Caso 2. Quanto o Imóvel é de Terceiro e está Alugado**

Repetir os passos 1 e 2 do caso anterior.

Ao cadastrar o evento financeiro ao invés de informar o Contrato de Administração informe o Contrato de Locação.

.

1. 1. Quando o evento for "**Agregado"** o valor referente a despesa irá compor o valor líquido do Aluguel através da inclusão de um valor de integração no laçamento financeiro, conforme informado no cadastro do tipo de Evento, mas se os lançamentos de aluguel já tiverem sido gerados é necessário que sejam RE-gerados.

Depois de incluir o Evento "Agregado" acesse o menu de contrato de locação, selecione o contrato em questão e gere novamente os lançamentos financeiro com data de vencimento >= ao vencimento da Parcela Agregada. Menu Processos → Gerar Lançamentos Financeiros.

Desta forma o sistema incluirá na cobrança de aluguel o valor do evento.

**Caso 3. Quanto o Imóvel é Próprio e está Alugado (Vacância)**

No cadastro do Imóvel MARQUE a opção*"Imóvel de propriedade da *administradora*de Imóvel?*" indicando que este imóvel é de propriedade da Administradora;

Não é necessário cadastrar o Cadastro de Administração.

Cadastre o Contrato e Locação e no Cadastrado do Evento Financeiro informe o número.

O Tratamento para o *"Tipo de Cobrança do Evento"* (Avulso ou Agregado) é o mesmo do caso anterior.

### Restrições

* Quando o Imóvel é próprio e não está alugado, não há necessidade de cadastrar o evento financeiro, pois a despesa será lançada no financeiro do BackOffice quando o documento fiscal entrar no sistema. Recomenda-se que seja criado um centro de custo para cada imóvel, pois desta forma será possível apurar as despesas de cada imóvel através de relatórios usando o centro de custo.
* Se uma despesa for parcelada em vários meses não há como criar um único evento financeiro que cobre do Locador quando o imóvel estiver Vago, e depois passe a cobrar do Locatário depois de alugado. *(se houver esta demanda, um ticket de melhoria deve ser criado)*
