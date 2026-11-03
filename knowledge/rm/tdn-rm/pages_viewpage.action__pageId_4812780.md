---
content_hash: 4971550e726c6be68e21f4b035a48b33da6511ed05ccf8ef9e9a1237b8ab78b0
fetched_at: '2026-06-29T00:10:18.916089+00:00'
page_id: '4812780'
product: rm
source: tdn-rm
title: Parametrização de Pensão Alimentícia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4812780
version: 4
---

BLOCK

Parametrização de Pensão Alimentícia

FAQ: **Parametrização de Pensão Alimentícia**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.0 e posteriores |

Avaliação

**Produto:** TOTVS Folha de Pagamento **Versão:** 11.20  
**Processo de Negocio:** Folha de Pagamento  
**Processo do Sistema:** Pensão Alimentícia  
**Subprocesso:**

Como parametrizar o sistema para cálculo da Pensão Alimentícia.

Solução

Procedimento:  
**1º Passo:** Acessar o módulo "Cadastros | Eventos".

[![image](http://lh6.ggpht.com/-uG70Xcl4SE8/T3SBPuzDCzI/AAAAAAAANL0/Am0UpDMQCLc/image_thumb%25255B3%25255D.png?imgmax=800 "image")](http://lh5.ggpht.com/-Rje5F_Z-Deg/T3SBOY-PsXI/AAAAAAAANLs/lJtl__hu704/s1600-h/image%25255B7%25255D.png)

Verificar se já existem os eventos de pensão alimentícia como descrito abaixo.  
Código de cálculo 13 - Pensão Alimentícia - Desconto do tipo valor.  
Código de cálculo 113 - Pensão Alimentícia nas Férias - Desconto do tipo valor.  
Código de cálculo 120 - Pensão Alimentícia na 2ª parcela de 13º salário- Desconto do tipo valor.  
Código de cálculo 121 - Pensão Alimentícia sobre participação nos lucros - Desconto do tipo valor.  
Caso não existam os eventos com as especificações acima cadastre dos mesmos.  
  
**2º Passo:** Marcar "Incidências de pensão" em cada evento que será considerado para determinado  
cálculo da pensão alimentícia.

Exemplo:  
Evento com Código de Calculo 2 - Dias trabalhados incidirá para cálculo de pensão na folha então  
deverá marcar na opção "Incidências de pensão" o item "Folha".

[![image](http://lh5.ggpht.com/-ZEEYHLxxVPE/T3SBSNwIT2I/AAAAAAAANME/88mIJVofdL0/image_thumb%25255B7%25255D.png?imgmax=800 "image")](http://lh5.ggpht.com/-DdsIGundWLQ/T3SBRAnQURI/AAAAAAAANL8/U6dxkdIxYwA/s1600-h/image%25255B15%25255D.png)

Dica:  
O evento com Código de Calculo 38 – Férias incidirá para cálculo de pensão nas férias então deverá  
marcar em "Incidências de pensão" o item "Férias".

**3º Passo:** Acessar o módulo "Cadastros | Tabelas Dinâmicas"

[![image](http://lh4.ggpht.com/-SPej9DylERU/T3SBU3twTFI/AAAAAAAANMU/E8FUAaGnGgU/image_thumb%25255B10%25255D.png?imgmax=800 "image")](http://lh4.ggpht.com/-0u5ItXClMYg/T3SBTU1-wnI/AAAAAAAANMM/7_dkq99W17k/s1600-h/image%25255B20%25255D.png)

Na tabela dinâmica "INT42" (Tipo de Código fixo) cadastrar a opções de Tipos de Códigos Fixos que  
poderão ser utilizados para desconto da Pensão. Ex: 13º Salário, Rescisão.

Observação: Caso estes já existam não é necessário cria-los novamente.

[![image](http://lh5.ggpht.com/-tYRjVFnlnBw/T3SBXXzT8JI/AAAAAAAANMk/Sy2pRF3qPoU/image_thumb%25255B14%25255D.png?imgmax=800 "image")](http://lh5.ggpht.com/-OygabSRPcds/T3SBWe1LwII/AAAAAAAANMc/353Mzjr2f3M/s1600-h/image%25255B26%25255D.png)

4º Passo: Acessar o módulo "Opções | Parâmetros | RM Labore"

[![image](http://lh4.ggpht.com/-wmIuHvTcB_Y/T3SBZifls6I/AAAAAAAANM0/1-lW1K8k_B0/image_thumb%25255B16%25255D.png?imgmax=800 "image")](http://lh3.ggpht.com/-yJjXBmsjE5w/T3SBYQ5dQBI/AAAAAAAANMs/_08LcZrLzm8/s1600-h/image%25255B30%25255D.png)

Na pasta "13º Salário | Códigos fixos" e marcar o tipo de código fixo criado no passo anterior.

[![image](http://lh3.ggpht.com/-6s_gtMUF2UQ/T3SBbYM1jLI/AAAAAAAANNE/Pk88BYyP1Kk/image_thumb%25255B19%25255D.png?imgmax=800 "image")](http://lh6.ggpht.com/-hijOHeAwgtw/T3SBaXzIcHI/AAAAAAAANM8/_Wn9V-T6rQ0/s1600-h/image%25255B35%25255D.png)

**5º Passo:** Marcar em "Opções | Parâmetros | RM Labore", pasta "Param. Rescisão | Código Fixo" e  
marcar o tipo de código fixo relacionado a pensão.

[![image](http://lh6.ggpht.com/-yMhy8zvE_6A/T3SBdM-dTfI/AAAAAAAANNU/l613JZDED4o/image_thumb%25255B22%25255D.png?imgmax=800 "image")](http://lh6.ggpht.com/-Hp9S4Gdw3nw/T3SBcRS8iHI/AAAAAAAANNM/U7uf1WlOOvI/s1600-h/image%25255B40%25255D.png)

**6º Passo:** Acesse o cadastro do funcionário que vai efetuar pagamento de pensão e localize a pasta  
"Base de Cálculo | Dependentes". Edite o cadastro do dependente e na pasta "Incidências" marque  
a incidência de Pensão.

[![image](http://lh4.ggpht.com/-p2GgVDhm6AQ/T3SBfe5qXoI/AAAAAAAANNk/aC8s6DOvvu0/image_thumb%25255B26%25255D.png?imgmax=800 "image")](http://lh4.ggpht.com/-uI4VOfLsJDs/T3SBeadu3-I/AAAAAAAANNc/BbL8qWQi_GI/s1600-h/image%25255B48%25255D.png)

**7º Passo:** Acesse no mesmo cadastro do dependente a pasta "Dados da pensão". Nesta pasta você  
vai informar a forma como o sistema deve calcular a pensão.

1 - Informe no campo "Percentual" o percentual da pensão.  
2 - Caso algum valor deva ser somado ao cálculo da pensão informe a fórmula com este valor no  
campo "Fórmula adicional de pensão".  
3 - Marque o campo "Ordenado Bruto" caso o queira considerar como base de calculo da pensão  
o valor bruto do salário do funcionário, caso o parâmetro fique desmarcado o sistema ira  
considerar o valor liquido do salário do funcionário.

[![image](http://lh5.ggpht.com/-B6RAVLRYIHo/T3SBiDQc0rI/AAAAAAAANN0/sTcJtYzZNBw/image_thumb%25255B30%25255D.png?imgmax=800 "image")](http://lh3.ggpht.com/-QBBcPE-rjRQ/T3SBgzRXjJI/AAAAAAAANNs/KMux-0umFBY/s1600-h/image%25255B56%25255D.png)

**8º Passo:** Caso exista algum evento que não deva ser considerado no cálculo da pensão informe  
este evento na pasta "Eventos não considerados".

[![image](http://lh5.ggpht.com/-o-D7Jqii2jE/T3SBj0r1DQI/AAAAAAAANOE/8JV4_Crvjmg/image_thumb%25255B34%25255D.png?imgmax=800 "image")](http://lh5.ggpht.com/-8EAZpiynMYA/T3SBi-qN4-I/AAAAAAAANN8/_qgrSSGgsoQ/s1600-h/image%25255B64%25255D.png)

**9 º Passo:** Acesse o cadastro do funcionário que vai efetuar pagamento de pensão e localize a pasta  
"Base de Cálculo | Códigos Fixos". Cadastre os eventos com Código de Cálculo 13 como Código Fixo  
Tipo Folha ou Folha/Rescisão (caso deseje descontar a pensão também na rescisão) e Código de  
Cálculo 120 como Código Fixo Tipo 13ª Salário.

[![image](http://lh5.ggpht.com/-_cHWD_9zXxc/T3SBlz6pOEI/AAAAAAAANOU/97VkAqWifDY/image_thumb%25255B36%25255D.png?imgmax=800 "image")](http://lh4.ggpht.com/-SnOerT_I-sM/T3SBk_Vc8PI/AAAAAAAANOM/31_p13e0Wqk/s1600-h/image%25255B68%25255D.png)

**10 º Passo:** Acesse: Movimento | Folha de Pagamento | Lançamentos Automáticos | Grupo de  
Eventos.

[![image](http://lh3.ggpht.com/-V8qrulb_040/T3SBnnjEy0I/AAAAAAAANOk/3ScVA2Nd84M/image_thumb%25255B40%25255D.png?imgmax=800 "image")](http://lh3.ggpht.com/-BZdUAHQabjI/T3SBmm7UABI/AAAAAAAANOc/5MaEJG72VR8/s1600-h/image%25255B76%25255D.png)

Edite um Grupo de Eventos e na pasta Códigos Fixos marque o Código Fixo Folha utilizado no 9º  
Passo, para que o evento Código de Cálculo 13 seja lançado no Envelope de Pagamento do  
funcionário.

[![image](http://lh5.ggpht.com/-K0vPITZiv4M/T3SBpljOTDI/AAAAAAAANO0/hg4R5EBI9z0/image_thumb%25255B42%25255D.png?imgmax=800 "image")](http://lh4.ggpht.com/-1JfW391Tylk/T3SBoR7itmI/AAAAAAAANOs/ZN6V3FHQmUQ/s1600-h/image%25255B78%25255D.png)

Ao realizar o lançamento do Grupo de Eventos marque na pasta Identificação marque a opção  
“Lança Codigos Fixos”, salve as alterações e faça o lançamento.

[![image](http://lh5.ggpht.com/-1AZOQEeFGAo/T3SBrc8rH8I/AAAAAAAANPE/B1YD7yUNFg0/image_thumb%25255B44%25255D.png?imgmax=800 "image")](http://lh4.ggpht.com/--eycZOXOInU/T3SBqWLKAxI/AAAAAAAANO8/NnNZoBACu8o/s1600-h/image%25255B82%25255D.png)

**11 º Passo:** Caso deseje descontar Pensão nas Férias, cadastre o evento de CC 113 - Pensão  
alimentícia nas férias em Cadastros | Funcionários | Férias | Adicionais Férias.

[![image](http://lh5.ggpht.com/-NztXvmKKmOI/T3SBtiwuIFI/AAAAAAAANPU/QzUWeSmUTvg/image_thumb%25255B47%25255D.png?imgmax=800 "image")](http://lh5.ggpht.com/-7nhJbdHTMVM/T3SBstp-sOI/AAAAAAAANPM/L7fhVc90Fl8/s1600-h/image%25255B87%25255D.png)

Ao lançar as férias será calculado o valor da pensão alimentícia nas férias, conforme  
parametrização do 7ª Passo.

**12 º Passo:** Ao lançar a rescisão marque a opção de lançar códigos fixos e será lançado, conforme parametrização do 7ª Passo a pensão alimentícia que estiver marcada para lançar em rescisão, caso não esteja cadastrado em código fixo para lançamento em rescisão o usuário deverá lançar manualmente todos os eventos de CC 13 - Pensão alimentícia, CC 113 - Pensão alimentícia nas férias, CC 120 - Pensão alimentícia s/ 13º salário e/ou CC 121 - Pensão alimentícia s/ participação nos lucros.

[![image](http://lh3.ggpht.com/-SSfQUP7_uOY/T3SBvYfR1HI/AAAAAAAANPk/lDMplkWBEzQ/image_thumb%25255B50%25255D.png?imgmax=800 "image")](http://lh5.ggpht.com/-XvBekWQ1OKc/T3SBuej7bkI/AAAAAAAANPc/HtF08dCRIgI/s1600-h/image%25255B92%25255D.png)

**13 º Passo:** Ao lançar o 13º salário marque a opção lançar códigos fixos e será lançado, conforme parametrização do 7ª Passo a pensão alimentícia sobre o 13º salário.

Observação: Para que o sistema calcule a pensão alimentícia sobre a 1ª parcela de 13º salário nas férias é necessário informar o evento com CC(120) – Pensão Alimentícia de 13º salário no campo Evento adicional de Férias.

Este evento não poderá estar informado nos Eventos Adicionais Globais de 13º Salário.

[![image](http://lh4.ggpht.com/-C2IXDAnIgms/T3SBw5swVEI/AAAAAAAANP0/hdQ6YJ78T6o/image_thumb%25255B55%25255D.png?imgmax=800 "image")](http://lh5.ggpht.com/-cEVqOsC5H-4/T3SBwA3QhTI/AAAAAAAANPs/Sz2duuKtsaI/s1600-h/image%25255B103%25255D.png)
