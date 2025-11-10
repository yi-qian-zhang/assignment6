import unittest
import platform
import hashlib

if __name__ == "__main__":
    from submission import part_1_a, part_2_a
    from submission import viterbi, multidimensional_viterbi


if platform.system() == 'Windows':
    NIX = False
    print("Test on Windows system")
else:
    NIX = True
    print("Test on Linux/OS X system")

def print_success_message(test_case):
    print("UnitTest {0} passed successfully!".format(test_case))

class TestPart1a(unittest.TestCase):        

    def test_prior(self, part_1_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_1_a()

        a_prior = sum(a_prior_probs.values())
        n_prior = sum(n_prior_probs.values())
        s_prior = sum(s_prior_probs.values())
        total_prob = a_prior + n_prior + s_prior 
        msg = ('incorrect prior probs. each word should be selected with '
               'equal probability. counted {}, should be 1').format(total_prob)
        self.assertAlmostEqual(1.0, total_prob, places=2, msg=msg)

        self.assertEqual('9b7483b9cce483802f467c912a262a2618ec36cb00ff364e62839f87a1a575c9', hashlib.sha256(str.encode(str(a_prior_probs["A1"]))).hexdigest(), msg='Incorrect a_prior_probs')

        self.assertEqual('9b7483b9cce483802f467c912a262a2618ec36cb00ff364e62839f87a1a575c9', hashlib.sha256(str.encode(str(n_prior_probs["N1"]))).hexdigest(), msg='Incorrect n_prior_probs')

        self.assertEqual('9b7483b9cce483802f467c912a262a2618ec36cb00ff364e62839f87a1a575c9', hashlib.sha256(str.encode(str(s_prior_probs["S1"]))).hexdigest(), msg='Incorrect s_prior_probs')

        print_success_message("test_prior")

    def test_a_emission(self, part_1_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_1_a()
        
        mean, std = a_emission_paras['A1']
        mean_hash = hashlib.sha256(str.encode(str(mean))).hexdigest()
        std_hash = hashlib.sha256(str.encode(str(std))).hexdigest()
        msg = 'incorrect mean for word ALLIGATOR, state A1'
        self.assertEqual("dc4e642e57357e0f1cb1b5d00322eaa03504e5345086df408e00c535d92c5c1c", mean_hash, msg)
        msg = 'incorrect std for word ALLIGATOR, state A1'
        self.assertEqual("7b40b9d0cc4a93e70b404b31441d8b6ad4baa9be85cdf1c87ac68b2dc2cac4e2", std_hash, msg)

        mean, std = a_emission_paras['A2']
        mean_hash = hashlib.sha256(str.encode(str(mean))).hexdigest()
        std_hash = hashlib.sha256(str.encode(str(std))).hexdigest()
        msg = 'incorrect mean for word ALLIGATOR, state A2'
        self.assertEqual("d848b818c065e37696a5a83b31f90b150dada7aff3159e9a801f9eab3f84543d", mean_hash, msg)
        msg = 'incorrect std for word ALLIGATOR, state A2'
        self.assertEqual("71b38a71dadf474805c1fb838ab0aac30a2be73fb8ae540990f362099ec0458a", std_hash, msg)

        mean, std = a_emission_paras['A3']
        mean_hash = hashlib.sha256(str.encode(str(mean))).hexdigest()
        std_hash = hashlib.sha256(str.encode(str(std))).hexdigest()
        msg = 'incorrect mean for word ALLIGATOR, state A3'
        self.assertEqual("c6fdb4c7c781483ed5058275d45bc68a335126c34bfb1849b63d0875b2666e82", mean_hash, msg)
        msg = 'incorrect std for word ALLIGATOR, state A3'
        self.assertEqual("de918c34fd162b7235733b7c81d76b202b010c490944a2e360ba275904a3b0cd", std_hash, msg)
        
        print_success_message("test_a_emission")

    def test_n_emission(self, part_1_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_1_a()

        mean, std = n_emission_paras['N1']
        mean_hash = hashlib.sha256(str.encode(str(mean))).hexdigest()
        std_hash = hashlib.sha256(str.encode(str(std))).hexdigest()
        msg = 'incorrect mean for word NUTS, state N1'
        self.assertEqual("af3861357513c7595874a57074a58a98526e1cb8ad5a71e8497bcb5b857f4ae2", mean_hash, msg)
        msg = 'incorrect std for word NUTS, state N1'
        self.assertEqual("aea25c614f99bcddaa58a6178a99569d16b5340ed0a6c96901c6723cb1a66e45", std_hash, msg)

        mean, std = n_emission_paras['N2']
        mean_hash = hashlib.sha256(str.encode(str(mean))).hexdigest()
        std_hash = hashlib.sha256(str.encode(str(std))).hexdigest()
        msg = 'incorrect mean for word NUTS, state N2'
        self.assertIn(mean_hash, ["53519e43db90bd08ff4459fd23fc944324ffb7d8f542ccc0b44257afea2ef525", "73475cb40a568e8da8a045ced110137e159f890ac4da883b6b17dc651b3a8049"], msg)
        msg = 'incorrect std for word NUTS, state N2'
        self.assertEqual("4dacbdf481f77b7385d1c5f286f306a3ef539dff02a0d0dbfccc17787705d0d0", std_hash, msg)

        mean, std = n_emission_paras['N3']
        mean_hash = hashlib.sha256(str.encode(str(mean))).hexdigest()
        std_hash = hashlib.sha256(str.encode(str(std))).hexdigest()
        msg = 'incorrect mean for word NUTS, state N3'
        self.assertIn(mean_hash, ["db58b6c40698d7371bbcff35d085e1bac5fa439d0de31eb8e0da7c47d27cb2a7", "39fa9ec190eee7b6f4dff1100d6343e10918d044c75eac8f9e9a2596173f80c9"], msg)
        msg = 'incorrect std for word NUTS, state N3'
        self.assertEqual("a0ac9b3dd38eecb310fa7e583d5ee2bce6236929a5e448d3d3c6b7c13a11900c", std_hash, msg)

        print_success_message("test_n_emission")

    def test_s_emission(self, part_1_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_1_a()
        
        mean, std = s_emission_paras['S1']
        mean_hash = hashlib.sha256(str.encode(str(mean))).hexdigest()
        std_hash = hashlib.sha256(str.encode(str(std))).hexdigest()
        msg = 'incorrect mean for word SLEEP, state S1'
        self.assertEqual("4defe1195908e76e51b32b81be42e655866e945ee168ece57bc5d53f1d0cf19e", mean_hash, msg)
        msg = 'incorrect std for word SLEEP, state S1'
        self.assertEqual("f975422fc861c785d6c6344981c501b2d3bda4d03e0d9f324481ef48c5f3e19f", std_hash, msg)

        mean, std = s_emission_paras['S2']
        mean_hash = hashlib.sha256(str.encode(str(mean))).hexdigest()
        std_hash = hashlib.sha256(str.encode(str(std))).hexdigest()
        msg = 'incorrect mean for word SLEEP, state S2'
        self.assertEqual("36b74139bd0ea465f5a1062708326be6402674312779940be0b99ba62d9f8cf3", mean_hash, msg)
        msg = 'incorrect std for word SLEEP, state S2'
        self.assertEqual("0d921877e5dd1b8b0458b49f422864b18180b6fb3ddc6b09c084f63f6fa661f9", std_hash, msg)

        mean, std = s_emission_paras['S3']
        mean_hash = hashlib.sha256(str.encode(str(mean))).hexdigest()
        std_hash = hashlib.sha256(str.encode(str(std))).hexdigest()
        msg = 'incorrect mean for word SLEEP, state S3'
        self.assertEqual("b7fc4a01285fb271d40e71eb0edde2b81de0df4282f24b657723559e9a6e0746", mean_hash, msg)
        msg = 'incorrect std for word SLEEP, state S3'
        self.assertEqual("d4e5ecf40ba5700a6c7c4a8ecac409c04f0bb0c85645e22e8a1899615637a649", std_hash, msg)

        print_success_message("test_s_emission")

    def test_a_transition(self, part_1_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_1_a()

        A1 = a_transition_probs['A1']

        possibleA1 = ['39e232e3ee1d0e8df9d234e61ddfeb1441c71d95dcc0193ed504d254f0582dac', '68e2a3a347603ff118d30a7f9cab414bf7f4120a0f6b2448385a2dea643dc716', '9b9075499bc920a1d807847f1a152695b60dcb0852144589308fdf613ad6993f', '74224d69e6b47bac5e15ee01a4d389a3608caf5f17a231d57550d9f51b59c927', '38a509f399834a25cbaea1deee03efeff30ff23fb8a82d68c1b16b2c8df8ec31']

        self.assertIn(hashlib.sha256(str.encode(str(A1["A1"]))).hexdigest(), possibleA1, msg='Incorrect A1 transition probabilities')

        possibleA2 = ['98ae7e1a1c969000c00251e26fcd88490716782274b110e852c6294c4569a023', '762f5fee46edfd75c85ae0573b023b36a0a4c1f4306bcb21159841e895257bbb', '91bf63946d645f5376722a19d6c010058c74383c94f5e19f1731ec26bf03ee31', 'b71ab84569ce34c6f330c14f3e55770bb917bf823ce71ee59dde31cbc13d358f', 'f6c1a2f88e5799f937d6d79ff9281d14b268911612d9808d7c07fb28fd33b74b']

        self.assertIn(hashlib.sha256(str.encode(str(A1["A2"]))).hexdigest(), possibleA2, msg='Incorrect A1 transition probabilities')

        possibleA2 = ['58eea32dc964880ee249620a8324602a3f2b6996c3e406357584fbed69f4cec3', 'a4b2c3a0b8e876d53b0a67a5847653c3c9d240b1a44f24f80720a34d15954ff7', 'e9f59eddfced6f0190c5f388808f99163162cfbe51ff068c52ba544b38c3004c', '147a3ec42b5ec65943bd6105a0ced239e2d853f9b62dc03d94491a54f592b033', 'd184edb29edf11cf7e6612f3f1357a8853e92a56c33c5eb9c5cb8ca763580d04']
        A2 = a_transition_probs['A2']
        self.assertIn(hashlib.sha256(str.encode(str(A2["A2"]))).hexdigest(), possibleA2, msg='Incorrect A2 transition probabilities')

        possibleA3 = ['891ca78469d9c7812a84eb6cbda0f11041bd0c4089c8b1ae9efafae5a9415a85', 'e2fa2c51faab39310ff61b5382295746a68de23828dc4a2f693dcfd02ed27f50', 'afd9f7f1ee7bc879ed6f2be2438a736480ddea7fe6806853682709ebfe11b3fe', '2ef73ef088a04dccb5be2b97b9a0fe3149a497f3649e1eb3ba8a573e981a9987', 'd845986c2c3637c324e89d243b7f137f0ee0de9791f32e088cf6c2d80fe97351']

        self.assertIn(hashlib.sha256(str.encode(str(A2["A3"]))).hexdigest(), possibleA3, msg='Incorrect A2 transition probabilities')

        possibleA3 = ['57c4ee9ec914a30d8f5ce0882bf7f96690f1b050dd04221a5be8e66e1b5130e0', '12929222a99ed27b0d3fb65266bfbc5031438d513b6864bcae417be5fcf5e6aa', 'def47d6bf65dd3236d343fe86ca3a77d73b36e5333391b545f749db105600252', '5c4d0571b75207ad4c169ce21a8f33aaac5c966c4362e11ac9080c8483d991ae', '1edfc6ad18a66c847658f50bbb8173eaf40203fa9a6b2e603ae7510ac02da736']
        A3 = a_transition_probs['A3']
        self.assertIn(hashlib.sha256(str.encode(str(A3["A3"]))).hexdigest(), possibleA3, msg='Incorrect A3 transition probabilities')

        pEnd = ['3a46e5d357db844905778c70778aa369978aea35863c3c9ca012393ffb3f7f2c', '9c7af113ac5e7751f7ebee02a00eef19700fdf99e20508d42744f4f4a5ef73fa', '258efd13f5e66fe01ceb80ed6a6028b66d285db42d80854a2bf7bdfe5385c148', 'f3b65c030f0f6b8f7992e0a26dcf28762ac81b06b20032fd16465d098379d5fc', 'd8e713637302f2df3585b1cda29dfa5c5091266c2199f4270dd22606e198998d']

        self.assertIn( hashlib.sha256(str.encode(str(A3["Aend"]))).hexdigest(), pEnd, msg='Incorrect A3 transition probabilities')

        Aend = a_transition_probs['Aend']
        self.assertEqual('d0ff5974b6aa52cf562bea5921840c032a860a91a3512f7fe8f768f6bbe005f6', hashlib.sha256(str.encode(str(Aend["Aend"]))).hexdigest(), msg='Incorrect Aend transition probabilities')

        print_success_message("test_a_transition")

    def test_n_transition(self, part_1_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_1_a()

        N1 = n_transition_probs['N1']
        N2 = n_transition_probs['N2']
        N3 = n_transition_probs['N3']
        Nend = n_transition_probs['Nend']

        n1n1 = ['c9a6613c0fd1607693473042d3e2cfbf710389c63e4082d9168cc1189da5b766', 'fdee4ed13c51cdb02e6d3c7b21492795ae80e408f77d94685663e1fd302ab238', 'd346a228477bd5d03fd550f6e2d34c54cd1b1d990eb5449043cadb737f38192a', 'b93df9bd32a825dd7751389f0d4e987807a8588357762d1a4f257f7be811879f', 'af83e05e96b869cab105fdf201163c84e8a953ae17c50db344c3f58d7dd74a0b']
        n1n2 = ['a5943c54dd10036fbbb633058548e4b8a677ea21a10cd7f6b49506c1ea66cd0b', 'd7457e8d7144c480bdc91dba679637b5172dc724236f3346cf4834671fa26843', '7d0feca7c504ef49b5d5d12a7e6bf6939abec5b6e5ebf9775d557628ce11e6f7', '2cd0a31d569d8a678d546fde86faca70814616f74475fb105bcdf99c36fbf99c', '83e689e51a82d220423265569bbb7fe55bd3bc0780f9e82024f4bf1540147779']

        self.assertIn(hashlib.sha256(str.encode(str(N1["N1"]))).hexdigest(), n1n1, msg='Incorrect N1 transition probabilities')

        self.assertIn(hashlib.sha256(str.encode(str(N1["N2"]))).hexdigest(), n1n2, msg='Incorrect N1 transition probabilities')

        n2n2 = ['8aed642bf5118b9d3c859bd4be35ecac75b6e873cce34e7b6f554b06f75550d7', '1fbbe3d1f4ee78c2a525b49166377adaf18feb0cb4e952db89669a88d2f6e1a0', 'ff7b023626eec04bd4733d7df109beb50c646fa60c4ea13895f03326ca758d59', '57a7ed5c14c5426868cc32d41d158b3b8368128a7258c8999db83788cffff0f8', 'ffbbcc0eb97e497fd1615d6bdc70fb2c897e19e41870e5380f0cebec38c21bfa']

        n2n3 = ['d0ff5974b6aa52cf562bea5921840c032a860a91a3512f7fe8f768f6bbe005f6', '44652f05931c0b024d5bed5574cf0485b6d4941986466b3c6ee2426872f36da1', 'f7177ab982b66b5b83bb19f6b5265d74101c6340861e97439641068b3f6b7a3d', 'bf13f51d682e1d2dded0e77dff06efb7e2ff228f64cdd6906005776f8e02ef40', 'bb67a9f0c56e1288692edaa3e734bb7c166d85fa2dbdcd412ac2bd7ef4e5988e']

        self.assertIn(hashlib.sha256(str.encode(str(N2["N2"]))).hexdigest(), n2n2, msg='Incorrect N2 transition probabilities')

        self.assertIn(hashlib.sha256(str.encode(str(N2["N3"]))).hexdigest(), n2n3, msg='Incorrect N2 transition probabilities')

        n3n3 = ['2c2a48ef50bda043845f29760fc070e955c2090951bbc69c5db07938169d83aa', '0c88d102dc52e577eef2b83c57d70a468bf3725c4d5cfb6295d8086973019b9c', '42c2fafec1898f65fdb9c7c4023b4d9df291550d8633028ba1be087a5a3a0715', '2ef73ef088a04dccb5be2b97b9a0fe3149a497f3649e1eb3ba8a573e981a9987', '8a2ba5db57dd6394d4e7b3564ed7c12e8bb24e6cbe089c8590c7547c2518b0ac']
        n3ne = ['062dc4dd611e417f34b0c33a7f1835c05e22cfa53dd759b74508d315f4037dfd', '17b5a9d9fd8e1bee36aa934dc1fa1a44b7b2e4192f54f6895218b1bdcdb8ded1', '953130c1fda9c8509c43c2474717528708f6a21d2fd2c6ebdf1fcd6eeafeb47b', '147a3ec42b5ec65943bd6105a0ced239e2d853f9b62dc03d94491a54f592b033', 'd9e2d7dccb5bd1b90b88183c5c623ad927cc8dcd4f6e687441396bedbae81010']

        self.assertIn(hashlib.sha256(str.encode(str(N3["N3"]))).hexdigest(), n3n3, msg='Incorrect N3 transition probabilities')

        self.assertIn(hashlib.sha256(str.encode(str(N3["Nend"]))).hexdigest(), n3ne, msg='Incorrect N3 transition probabilities')

        self.assertEqual('d0ff5974b6aa52cf562bea5921840c032a860a91a3512f7fe8f768f6bbe005f6', hashlib.sha256(str.encode(str(Nend["Nend"]))).hexdigest(), msg='Incorrect Nend transition probabilities')

        print_success_message("test_n_transition")

    def test_s_transition(self, part_1_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_1_a()

        S1 = s_transition_probs['S1']
        S2 = s_transition_probs['S2']
        S3 = s_transition_probs['S3']
        Send = s_transition_probs['Send']
        s1s1 = ['6b47421473460eb380a1eaadef064866a707b1e347dac2d10c993b58e91e715d', '2d9303cdc15f5e6ad8faab701c4f8e0c9de2a6701a60f28c3a03e31463ef3016', '13edbf90d092d8a14968788cb27b833f85fb5bc2f18b7739bca2945d18e0390d', 'dd7a194c8f2c5519d86333ee33067af559bf929536f16d3ebd06774ca0307f23', '42c2fafec1898f65fdb9c7c4023b4d9df291550d8633028ba1be087a5a3a0715']
        s1s2 = ['9df9112118a1cb584f5352a3175b371d8024a7d1e3bfb423d7ca5a646a1759a4', '81e7e8f82d02c067de1fc76fbf2b25d5752580da34be42b99c49487cc2ca6676', '4e143f1c6e0b0d15dce57d0ef11b9933fe9c98f15ae9ec0c3207aae0ed620f2c', 'e08c3ff4c932c4da59d450c57767574cfd19388b3c699015490afdcfb21fc414', '953130c1fda9c8509c43c2474717528708f6a21d2fd2c6ebdf1fcd6eeafeb47b']

        self.assertIn(hashlib.sha256(str.encode(str(S1["S1"]))).hexdigest(), s1s1, msg='Incorrect S1 transition probabilities')

        self.assertIn(hashlib.sha256(str.encode(str(S1["S2"]))).hexdigest(), s1s2, msg='Incorrect S1 transition probabilities')
        s2s2 = ['0f90e9f39d6650f5f1c8a43580dc9466f9258015f623ac5345f358ae45d26f14', 'debb42eb6b485fd14e0b7e3cc0e7fd446e2bad5ce8f0448d120456502a007447', 'fc803c48b002825e317b319196b312691a7f802a4b06bf19ba0de489560756c0', 'cbe4acd2532c89433c3e0fde332c89467c2356b2a0c8013e414949bb175dee82', '9cc3f72db2ed032859d8f23fc2dd39a5d6c71bca5f6108c1becdb34afc07bf9b']
        s2s3 = ['aa8b691ec6631efe9d155cd2a4ff6b44f111ca52a98600efe8960cf3af4f52b7', 'd2f8292d014cfce3eeee0a5c190fd1837343ed0aee7ba3ebc85eef9b71cb9382', 'e81b6a110a55335b0abee3768d545455b2d94d67cd383f3112ba48128f9b733f', 'a65ed1b23eaf7c24f8f802cc1d647531177252309dc078ae0cff72da1a223cff', '376b78bd2983dbe9132f023dca4ca1870df23304b072299d8d201e0a64fc6f31']

        self.assertIn(hashlib.sha256(str.encode(str(S2["S2"]))).hexdigest(), s2s2, msg='Incorrect S2 transition probabilities')

        self.assertIn(hashlib.sha256(str.encode(str(S2["S3"]))).hexdigest(), s2s3, msg='Incorrect S2 transition probabilities')

        s3s3 = ['8aed642bf5118b9d3c859bd4be35ecac75b6e873cce34e7b6f554b06f75550d7', '1fbbe3d1f4ee78c2a525b49166377adaf18feb0cb4e952db89669a88d2f6e1a0', 'ff7b023626eec04bd4733d7df109beb50c646fa60c4ea13895f03326ca758d59', '57a7ed5c14c5426868cc32d41d158b3b8368128a7258c8999db83788cffff0f8', 'ffbbcc0eb97e497fd1615d6bdc70fb2c897e19e41870e5380f0cebec38c21bfa']

        s3se = ['d0ff5974b6aa52cf562bea5921840c032a860a91a3512f7fe8f768f6bbe005f6', '44652f05931c0b024d5bed5574cf0485b6d4941986466b3c6ee2426872f36da1', 'f7177ab982b66b5b83bb19f6b5265d74101c6340861e97439641068b3f6b7a3d', 'bf13f51d682e1d2dded0e77dff06efb7e2ff228f64cdd6906005776f8e02ef40', 'bb67a9f0c56e1288692edaa3e734bb7c166d85fa2dbdcd412ac2bd7ef4e5988e']

        self.assertIn(hashlib.sha256(str.encode(str(S3["S3"]))).hexdigest(), s3s3, msg='Incorrect S3 transition probabilities')

        self.assertIn(hashlib.sha256(str.encode(str(S3["Send"]))).hexdigest(),s3se, msg='Incorrect S3 transition probabilities')

        self.assertEqual('d0ff5974b6aa52cf562bea5921840c032a860a91a3512f7fe8f768f6bbe005f6', hashlib.sha256(str.encode(str(Send["Send"]))).hexdigest(), msg='Incorrect Send transition probabilities')

        print_success_message("test_s_transition")

class TestPart1b(unittest.TestCase):

    def setup(self, part_1_a):
        a_states = ['A1', 'A2', 'A3', 'Aend']
        n_states = ['N1', 'N2', 'N3', 'Nend']
        s_states = ['S1', 'S2', 'S3', 'Send']

        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_1_a()

        states = a_states + n_states + s_states
        prior = a_prior_probs
        prior.update(n_prior_probs)
        prior.update(s_prior_probs)

        trans = a_transition_probs
        trans.update(n_transition_probs)
        trans.update(s_transition_probs)

        emiss = a_emission_paras
        emiss.update(n_emission_paras)
        emiss.update(s_emission_paras)
        return states, prior, trans, emiss

    def test_viterbi_case1(self, part_1_a, viterbi):
        evidence = []
        states, prior, trans, emiss = self.setup(part_1_a)
        seq, prob = viterbi(evidence, states, prior, trans, emiss)
        msg = ('when evidence is an empty list, return "None" or [], '
                'got {}').format(seq)
        self.assertTrue(seq in [None, []], msg)
        msg = ('when evidence is an empty list, return prob=0.0, '
                'got {}').format(prob)
        self.assertTrue(prob == 0., msg)
        print_success_message("test_viterbi_case1")

    def test_viterbi_case2(self, part_1_a, viterbi):
        evidence = [30]
        prob_ans = 0.01576664562875057
        seq_ans = ['S1']
        states, prior, trans, emiss = self.setup(part_1_a)
        seq, prob = viterbi(evidence, states, prior, trans, emiss)
        self.assertAlmostEqual(prob_ans, prob, places=7)
        self.assertEqual(seq_ans, seq)
        print_success_message("test_viterbi_case2")


    def test_viterbi_case3(self, part_1_a, viterbi):
        evidence = [40]
        prob_ans = 0.011713950611283535
        seq_ans = ['N1']
        states, prior, trans, emiss = self.setup(part_1_a)
        seq, prob = viterbi(evidence, states, prior, trans, emiss)
        self.assertAlmostEqual(prob_ans, prob, places=7)
        self.assertEqual(seq_ans, seq)
        print_success_message("test_viterbi_case3")


    def test_viterbi_realsample1(self, part_1_a, viterbi):
        """
        Extracted from GISLR dataset: idx: 17; length: 8
        Actual words: ALLIGATOR
        """
        evidence = [20, 65, 20, 30, 45, 60, 60, 42]
        prob_ans = 5.739096406102214e-17
        seq_ans = ['A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1']
        states, prior, trans, emiss = self.setup(part_1_a)
        seq, prob = viterbi(evidence, states, prior, trans, emiss)
        self.assertAlmostEqual(prob_ans, prob, places=21)
        # print(seq)
        self.assertEqual(seq_ans, seq)
        print_success_message("test_viterbi_realsample1")


    def test_viterbi_realsample2(self, part_1_a, viterbi):
        """
        Extracted from GISLR dataset: idx: 8; length: 9
        Actual words: NUTS
        """
        evidence = [45, 35, 34, 44, 41, 42, 45, 46, 45]
        prob_ans = 4.968812725589942e-15
        seq_ans = ['N1', 'N1', 'N1', 'N1', 'N1', 'N1', 'N1', 'N1', 'N1']
        states, prior, trans, emiss = self.setup(part_1_a)
        seq, prob = viterbi(evidence, states, prior, trans, emiss)
        self.assertAlmostEqual(prob_ans, prob, places=19)
        self.assertEqual(seq_ans, seq)
        print_success_message("test_viterbi_realsample2")

    def test_viterbi_realsample3(self, part_1_a, viterbi):
        """
        Extracted from GISLR dataset: idx: 9; length: 12
        Actual words: SLEEP
        """
        evidence = [26, 22, 13, 26, 20, 31, 32, 39, 41, 42, 38, 40]
        prob_ans = 8.189507039078366e-20
        seq_ans = ['S1', 'S1', 'S1', 'S1', 'S1', 'S2', 'S2', 'S2', 'S2', 'S2', 'S2', 'S2']
        states, prior, trans, emiss = self.setup(part_1_a)
        seq, prob = viterbi(evidence, states, prior, trans, emiss)
        self.assertAlmostEqual(prob_ans, prob, places=24)
        self.assertEqual(seq_ans, seq)
        print_success_message("test_viterbi_realsample3")


class TestPart2a(unittest.TestCase):

    def test_prior(self, part_2_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_2_a()

        a_prior = sum(a_prior_probs.values())
        n_prior = sum(n_prior_probs.values())
        s_prior = sum(s_prior_probs.values())
        total_prob = a_prior + n_prior + s_prior
        msg = ('incorrect prior probs. each word should be selected with '
               'equal probability. counted {}, should be 1').format(total_prob)
        self.assertAlmostEqual(1.0, total_prob, places=2, msg=msg)
        print_success_message("test_prior")

    def test_a_emission(self, part_2_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_2_a()

        right, thumb = a_emission_paras['A1']
        rmean, rstd = right
        meanhash = hashlib.sha256(str.encode(str(rmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(rstd))).hexdigest()
        msg = 'incorrect mean for word ALLIGATOR, state A1, right hand'
        self.assertEqual("dc4e642e57357e0f1cb1b5d00322eaa03504e5345086df408e00c535d92c5c1c", meanhash, msg)
        msg = 'incorrect std for word ALLIGATOR, state A1, right hand'
        self.assertEqual("7b40b9d0cc4a93e70b404b31441d8b6ad4baa9be85cdf1c87ac68b2dc2cac4e2", stdhash, msg)

        tmean, tstd = thumb
        meanhash = hashlib.sha256(str.encode(str(tmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(tstd))).hexdigest()
        msg = 'incorrect mean for word ALLIGATOR, state A1, right thumb'
        self.assertEqual("baa978466aa5869be1e768e5f966864fb131df6332ac2723c7c9e45e809abd46", meanhash, msg)
        msg = 'incorrect std for word ALLIGATOR, state A1, right thumb'
        self.assertEqual("d1b9834fbc7fefd51ba26269bba48115cded772aa18055dbf695b39a3c209e00", stdhash, msg)

        right, thumb = a_emission_paras['A2']
        rmean, rstd = right
        meanhash = hashlib.sha256(str.encode(str(rmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(rstd))).hexdigest()
        msg = 'incorrect mean for word ALLIGATOR, state A2, right hand'
        self.assertEqual("d848b818c065e37696a5a83b31f90b150dada7aff3159e9a801f9eab3f84543d", meanhash, msg)
        msg = 'incorrect std for word ALLIGATOR, state A2, right hand'
        self.assertEqual("71b38a71dadf474805c1fb838ab0aac30a2be73fb8ae540990f362099ec0458a", stdhash, msg)

        tmean, tstd = thumb
        meanhash = hashlib.sha256(str.encode(str(tmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(tstd))).hexdigest()
        msg = 'incorrect mean for word ALLIGATOR, state A2, right thumb'
        self.assertEqual("b6015221de8797c036f5557bedccfebfa503cfd4b376403190a0afb0e14eba25", meanhash, msg)
        msg = 'incorrect std for word ALLIGATOR, state A2, right thumb'
        self.assertEqual("96764d799010a03690df003296bfe031b5d38a547e82986fc4b8c1ae18db1cdd", stdhash, msg)

        right, thumb = a_emission_paras['A3']
        rmean, rstd = right
        meanhash = hashlib.sha256(str.encode(str(rmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(rstd))).hexdigest()
        msg = 'incorrect mean for word ALLIGATOR, state A3, right hand'
        self.assertEqual("c6fdb4c7c781483ed5058275d45bc68a335126c34bfb1849b63d0875b2666e82", meanhash, msg)
        msg = 'incorrect std for word ALLIGATOR, state A3, right hand'
        self.assertEqual("de918c34fd162b7235733b7c81d76b202b010c490944a2e360ba275904a3b0cd", stdhash, msg)

        tmean, tstd = thumb
        meanhash = hashlib.sha256(str.encode(str(tmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(tstd))).hexdigest()
        msg = 'incorrect mean for word ALLIGATOR, state A3, right thumb'
        self.assertIn(meanhash, ["b690285b6e60662df771bc7a6b6ee1cb13f799e3d902ec40de8515a66438d851", "031b4af5197ec30a926f48cf40e11a7dbc470048a21e4003b7a3c07c5dab1baa"], msg)
        msg = 'incorrect std for word ALLIGATOR, state A3, right thumb'
        self.assertEqual("cef3814cc52a81bcdccdc7661756fb35525d837e0fad39a65717778e7c435d1e", stdhash, msg)
        print_success_message("test_a_emission")


    def test_n_emission(self, part_2_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_2_a()

        right, thumb = n_emission_paras['N1']
        rmean, rstd = right
        meanhash = hashlib.sha256(str.encode(str(rmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(rstd))).hexdigest()
        msg = 'incorrect mean for word NUTS, state N1, right hand'
        self.assertEqual("af3861357513c7595874a57074a58a98526e1cb8ad5a71e8497bcb5b857f4ae2", meanhash, msg)
        msg = 'incorrect std for word NUTS, state N1, right hand'
        self.assertEqual("aea25c614f99bcddaa58a6178a99569d16b5340ed0a6c96901c6723cb1a66e45", stdhash, msg)

        tmean, tstd = thumb
        meanhash = hashlib.sha256(str.encode(str(tmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(tstd))).hexdigest()
        msg = 'incorrect mean for word NUTS, state N1, right thumb'
        self.assertEqual("34b7997a98975663f8a40962e4648386a699414189ddfe871bb627f47a6d8289", meanhash, msg)
        msg = 'incorrect std for word NUTS, state N1, right thumb'
        self.assertEqual("171c5b45e9be9027b5d5da65d2c7b7120298d6575b48a8f0626d69f5eed4e639", stdhash, msg)

        right, thumb = n_emission_paras['N2']
        rmean, rstd = right
        meanhash = hashlib.sha256(str.encode(str(rmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(rstd))).hexdigest()
        msg = 'incorrect mean for word NUTS, state N2, right hand'
        self.assertIn(meanhash, ["53519e43db90bd08ff4459fd23fc944324ffb7d8f542ccc0b44257afea2ef525", "73475cb40a568e8da8a045ced110137e159f890ac4da883b6b17dc651b3a8049"], msg)
        msg = 'incorrect std for word NUTS, state N2, right hand'
        self.assertEqual("4dacbdf481f77b7385d1c5f286f306a3ef539dff02a0d0dbfccc17787705d0d0", stdhash, msg)

        tmean, tstd = thumb
        meanhash = hashlib.sha256(str.encode(str(tmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(tstd))).hexdigest()
        msg = 'incorrect mean for word NUTS, state N2, right thumb'
        self.assertIn(meanhash, ["db58b6c40698d7371bbcff35d085e1bac5fa439d0de31eb8e0da7c47d27cb2a7", "39fa9ec190eee7b6f4dff1100d6343e10918d044c75eac8f9e9a2596173f80c9"], msg)
        msg = 'incorrect std for word NUTS, state N2, right thumb'
        self.assertEqual("de4035033333a049be2abd5262d5453f8f0694de1e41230002cda288e426a73a", stdhash, msg)


        right, thumb = n_emission_paras['N3']
        rmean, rstd = right
        meanhash = hashlib.sha256(str.encode(str(rmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(rstd))).hexdigest()
        msg = 'incorrect mean for word NUTS, state N3, right hand'
        self.assertIn(meanhash, ["db58b6c40698d7371bbcff35d085e1bac5fa439d0de31eb8e0da7c47d27cb2a7", "39fa9ec190eee7b6f4dff1100d6343e10918d044c75eac8f9e9a2596173f80c9"], msg)
        msg = 'incorrect std for word NUTS, state N3, right hand'
        self.assertEqual("a0ac9b3dd38eecb310fa7e583d5ee2bce6236929a5e448d3d3c6b7c13a11900c", stdhash, msg)

        tmean, tstd = thumb
        meanhash = hashlib.sha256(str.encode(str(tmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(tstd))).hexdigest()
        msg = 'incorrect mean for word NUTS, state N3, right thumb'
        self.assertEqual("55aab5343179c1e94bd0bf77f520452e73dbe389e77a18495ff1b514c6a53372", meanhash, msg)
        msg = 'incorrect std for word NUTS, state N3, right thumb'
        self.assertEqual("f88baa407aa8ae899ac2d8974b93d1e0492e5fcd60dfe39d3fcd6dba67ffc281", stdhash, msg)
        print_success_message("test_n_emission")

    def test_s_emission(self, part_2_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_2_a()
        
        right, thumb = s_emission_paras['S1']
        rmean, rstd = right
        meanhash = hashlib.sha256(str.encode(str(rmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(rstd))).hexdigest()
        msg = 'incorrect mean for word SLEEP, state S1, right hand'
        self.assertEqual("4defe1195908e76e51b32b81be42e655866e945ee168ece57bc5d53f1d0cf19e", meanhash, msg)
        msg = 'incorrect std for word SLEEP, state S1, right hand'
        self.assertEqual("f975422fc861c785d6c6344981c501b2d3bda4d03e0d9f324481ef48c5f3e19f", stdhash, msg)

        tmean, tstd = thumb
        meanhash = hashlib.sha256(str.encode(str(tmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(tstd))).hexdigest()
        msg = 'incorrect mean for word SLEEP, state S1, right thumb'
        self.assertEqual("920d1688180b701cb8f7839f6323d0d0f6c0b9a4307e9c7adbf14d74f2ee94d7", meanhash, msg)
        msg = 'incorrect std for word SLEEP, state S1, right thumb'
        self.assertEqual("45902850d242885c22f2468cf352fce2324940d5e1456f3a89ef985e9bfa672a", stdhash, msg)

        right, thumb = s_emission_paras['S2']
        rmean, rstd = right
        meanhash = hashlib.sha256(str.encode(str(rmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(rstd))).hexdigest()
        msg = 'incorrect mean for word SLEEP, state S2, right hand'
        self.assertEqual("36b74139bd0ea465f5a1062708326be6402674312779940be0b99ba62d9f8cf3", meanhash, msg)
        msg = 'incorrect std for word SLEEP, state S2, right hand'
        self.assertEqual("0d921877e5dd1b8b0458b49f422864b18180b6fb3ddc6b09c084f63f6fa661f9", stdhash, msg)

        tmean, tstd = thumb
        meanhash = hashlib.sha256(str.encode(str(tmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(tstd))).hexdigest()
        msg = 'incorrect mean for word SLEEP, state S2, right thumb'
        self.assertEqual("4902fd1a892e4f093eb29a0cb97a3f9953f7b36146f6826de657c004667220ed", meanhash, msg)
        msg = 'incorrect std for word SLEEP, state S2, right thumb'
        self.assertEqual("f8947fae811b536d3c0d823bb88a7a66a8c5aad402e84e92bc2dc0ddc499e26d", stdhash, msg)

        right, thumb = s_emission_paras['S3']
        rmean, rstd = right
        meanhash = hashlib.sha256(str.encode(str(rmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(rstd))).hexdigest()
        msg = 'incorrect mean for word SLEEP, state S3, right hand'
        self.assertEqual("b7fc4a01285fb271d40e71eb0edde2b81de0df4282f24b657723559e9a6e0746", meanhash, msg)
        msg = 'incorrect std for word SLEEP, state S3, right hand'
        self.assertEqual("d4e5ecf40ba5700a6c7c4a8ecac409c04f0bb0c85645e22e8a1899615637a649", stdhash, msg)

        tmean, tstd = thumb
        meanhash = hashlib.sha256(str.encode(str(tmean))).hexdigest()
        stdhash = hashlib.sha256(str.encode(str(tstd))).hexdigest()
        msg = 'incorrect mean for word SLEEP, state S3, right thumb'
        self.assertEqual("e3adf5399c40c50de563e1e29e2ff9806db3e33d7d421903d5e7d9928236fd63", meanhash, msg)
        msg = 'incorrect std for word SLEEP, state S3, right thumb'
        self.assertEqual("8e546b2aec2423e1383dd5603f0a03cc0d53fcbaa60dc4f4acffc6d276dcae6f", stdhash, msg)
        print_success_message("test_s_emission")

    def test_a_transition(self, part_2_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_2_a()

        for state, probs in a_transition_probs.items():
            right, thumb = zip(*probs.values())

            msg = ('right hand ALLIGATOR transition prob in state {} '
                   'should sum to 1 (got {})').format(state, sum(right))
            self.assertAlmostEqual(1.0, sum(right), places=2, msg=msg)
            msg = ('right thumb ALLIGATOR transition prob in state {} '
                   'should sum to 1 (got {})').format(state, sum(thumb))
            self.assertAlmostEqual(1.0, sum(thumb), places=2, msg=msg)
        print_success_message("test_a_transition")

    def test_n_transition(self, part_2_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_2_a()
        
        for state, probs in n_transition_probs.items():
            right, thumb = zip(*probs.values())

            msg = ('right hand NUTS transition prob in state {} '
                   'should sum to 1 (got {})').format(state, sum(right))
            self.assertAlmostEqual(1.0, sum(right), places=2, msg=msg)
            msg = ('right thumb NUTS transition prob in state {} '
                   'should sum to 1 (got {})').format(state, sum(thumb))
            self.assertAlmostEqual(1.0, sum(thumb), places=2, msg=msg)
        print_success_message("test_n_transition")

    def test_s_transition(self, part_2_a):
        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_2_a()

        for state, probs in s_transition_probs.items():
            right, thumb = zip(*probs.values())

            msg = ('right hand SLEEP transition prob in state {} '
                   'should sum to 1 (got {})').format(state, sum(right))
            self.assertAlmostEqual(1.0, sum(right), places=2, msg=msg)
            msg = ('right thumb SLEEP transition prob in state {} '
                   'should sum to 1 (got {})').format(state, sum(thumb))
            self.assertAlmostEqual(1.0, sum(thumb), places=2, msg=msg)
        print_success_message("test_s_transition")

class TestPart2b(unittest.TestCase):
    def setup(self, part_2_a):
        a_states = ['A1', 'A2', 'A3', 'Aend']
        n_states = ['N1', 'N2', 'N3', 'Nend']
        s_states = ['S1', 'S2', 'S3', 'Send']

        (a_prior_probs, a_transition_probs, a_emission_paras,
        n_prior_probs, n_transition_probs, n_emission_paras,
        s_prior_probs, s_transition_probs, s_emission_paras) = part_2_a()

        states = a_states + n_states + s_states
        prior = a_prior_probs
        prior.update(n_prior_probs)
        prior.update(s_prior_probs)

        trans = a_transition_probs
        trans.update(n_transition_probs)
        trans.update(s_transition_probs)

        emiss = a_emission_paras
        emiss.update(n_emission_paras)
        emiss.update(s_emission_paras)
        return states, prior, trans, emiss

    def test_viterbi_case1(self, part_2_a, multidimensional_viterbi):
        evidence = []
        states, prior, trans, emiss = self.setup(part_2_a)
        seq, prob = multidimensional_viterbi(evidence,
                            states,
                            prior,
                            trans,
                            emiss)
        msg = ('when evidence is an empty list, return "None" or [], '
                'got {}').format(seq)
        self.assertTrue(seq in [None, []], msg)
        msg = ('when evidence is an empty list, return prob=0.0, '
                'got {}').format(prob)
        self.assertTrue(prob == 0., msg)

        print_success_message("test_viterbi_case1")

    def test_viterbi_case2(self, part_2_a, multidimensional_viterbi):

        evidence = [(50, 100)]
        prob_ans = 4.039157063192714e-06
        seq_ans = ['A1']

        states, prior, trans, emiss = self.setup(part_2_a)

        seq, prob = multidimensional_viterbi(evidence,
                                            states,
                                            prior,
                                            trans,
                                            emiss)
        self.assertAlmostEqual(prob_ans, prob, places=10)
        self.assertEqual(seq_ans, seq)

        print_success_message("test_viterbi_case2")

    def test_viterbi_case3(self, part_2_a, multidimensional_viterbi):
        evidence = [(40, 40)]
        prob_ans = 0.0005593481817454066
        seq_ans = ['N1']

        states, prior, trans, emiss = self.setup(part_2_a)

        seq, prob = multidimensional_viterbi(evidence,
                                            states,
                                            prior,
                                            trans,
                                            emiss)
        self.assertAlmostEqual(prob_ans, prob, places=8)
        self.assertEqual(seq_ans, seq)

        print_success_message("test_viterbi_case3")

    def test_viterbi_realsample1(self, part_2_a, multidimensional_viterbi):
        """
        Extracted from GISLR dataset: idx: 17; length: 8
        Actual words: ALLIGATOR
        """
        right_hand_y = [20, 65, 20, 30, 45, 60, 60, 42]
        right_thumb_y = [56, 74, 48, 41, 38, 55, 56, 44]
        evidence = list(zip(right_hand_y, right_thumb_y))

        prob_ans = 2.4799888302784736e-31
        seq_ans = ['A1', 'A1', 'A2', 'A2', 'A2', 'A3', 'A3', 'A3']

        states, prior, trans, emiss = self.setup(part_2_a)

        seq, prob = multidimensional_viterbi(evidence,
                                            states,
                                            prior,
                                            trans,
                                            emiss)
        self.assertAlmostEqual(prob_ans, prob, places=35)
        self.assertEqual(seq_ans, seq)

        print_success_message("test_viterbi_realsample1")

    def test_viterbi_realsample2(self, part_2_a, multidimensional_viterbi):
        """
        Extracted from GISLR dataset: idx: 8; length: 9
        Actual words: NUTS
        """
        right_hand_y = [45, 35, 34, 44, 41, 42, 45, 46, 45]
        right_thumb_y = [44, 35, 38, 32, 31, 33, 39, 40, 39]
        evidence = list(zip(right_hand_y, right_thumb_y))

        prob_ans = 1.5475168339553707e-27
        seq_ans = ['N1', 'N1', 'N1', 'N1', 'N1', 'N1', 'N1', 'N1', 'N1']

        states, prior, trans, emiss = self.setup(part_2_a)

        seq, prob = multidimensional_viterbi(evidence,
                                            states,
                                            prior,
                                            trans,
                                            emiss)
        self.assertAlmostEqual(prob_ans, prob, places=31)
        self.assertEqual(seq_ans, seq)

        print_success_message("test_viterbi_realsample2")

    def test_viterbi_realsample3(self, part_2_a, multidimensional_viterbi):
        """
        Extracted from GISLR dataset: idx: 9; length: 12
        Actual words: SLEEP
        """
        right_hand_y = [26, 22, 13, 26, 20, 31, 32, 39, 41, 42, 38, 40]
        right_thumb_y = [32, 36, 31, 30, 25, 30, 29, 34, 31, 45, 35, 35]
        evidence = list(zip(right_hand_y, right_thumb_y))

        prob_ans = 3.3963665653580956e-38
        seq_ans = ['S1', 'S1', 'S1', 'S1', 'S1', 'S2', 'S2', 'S2', 'S2', 'S2', 'S2', 'S2']

        states, prior, trans, emiss = self.setup(part_2_a)

        seq, prob = multidimensional_viterbi(evidence,
                                            states,
                                            prior,
                                            trans,
                                            emiss)
        self.assertAlmostEqual(prob_ans, prob, places=42)
        self.assertEqual(seq_ans, seq)

        print_success_message("test_viterbi_realsample3")


if __name__ == "__main__":
    TestPart1a().test_prior(part_1_a)
    TestPart1a().test_a_emission(part_1_a)
    TestPart1a().test_n_emission(part_1_a)
    TestPart1a().test_s_emission(part_1_a)
    TestPart1a().test_a_transition(part_1_a)
    TestPart1a().test_n_transition(part_1_a)
    TestPart1a().test_s_transition(part_1_a)
    TestPart1b().test_viterbi_case1(part_1_a, viterbi)
    TestPart1b().test_viterbi_case2(part_1_a, viterbi)
    TestPart1b().test_viterbi_case3(part_1_a, viterbi)
    TestPart1b().test_viterbi_realsample1(part_1_a, viterbi)
    TestPart1b().test_viterbi_realsample2(part_1_a, viterbi)
    TestPart1b().test_viterbi_realsample3(part_1_a, viterbi)

    TestPart2a().test_prior(part_2_a)
    TestPart2a().test_a_emission(part_2_a)
    TestPart2a().test_n_emission(part_2_a)
    TestPart2a().test_s_emission(part_2_a)
    TestPart2a().test_a_transition(part_2_a)
    TestPart2a().test_n_transition(part_2_a)
    TestPart2a().test_s_transition(part_2_a)

    TestPart2b().test_viterbi_case1(part_2_a, multidimensional_viterbi)
    TestPart2b().test_viterbi_case2(part_2_a, multidimensional_viterbi)
    TestPart2b().test_viterbi_case3(part_2_a, multidimensional_viterbi)
    TestPart2b().test_viterbi_realsample1(part_2_a, multidimensional_viterbi)
    TestPart2b().test_viterbi_realsample2(part_2_a, multidimensional_viterbi)
    TestPart2b().test_viterbi_realsample3(part_2_a, multidimensional_viterbi)

